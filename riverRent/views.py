# Python imports
import json
from datetime import datetime
from pytz import timezone

# Django imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.core.serializers import serialize

# Local app imports
from .models import *

# Third party imports
from phonenumber_field.formfields import PhoneNumberField


# HTTP methods decorator
@require_http_methods(["GET"])
def index(request):
    """ Index view """
    
    return render(request, "riverRent/index.html")


# HTTP methods decorator
@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "riverRent/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "riverRent/login.html")


# HTTP methods decorator
@require_http_methods(["GET"])
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# HTTP methods decorator
@require_http_methods(["GET", "POST"])
def register(request):

    # Define phone form class
    class registerForm(forms.Form):
        usernameSubmit = forms.CharField(max_length=50, widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder":"Username"}
        ))
        firstnameSubmit = forms.CharField(max_length=64, widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder":"First Name"}
        ))
        lastnameSubmit = forms.CharField(max_length=64, widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder":"Last Name"}
        ))
        emailSubmit = forms.CharField(max_length=64, widget=forms.EmailInput(
            attrs={"class":"form-control", "placeholder":"Email Address"}
        ))
        passwordSubmit = forms.CharField(max_length=50, widget=forms.PasswordInput(
            attrs={"class":"form-control", "placeholder":"Password"}
        ))
        confirmationSubmit = forms.CharField(max_length=50, widget=forms.PasswordInput(
            attrs={"class":"form-control", "placeholder":"Confirm Password"}
        ))
        phoneSubmit = PhoneNumberField(widget=forms.NumberInput(
            attrs={"class":"form-control", "placeholder":"Phone [eg. +1 (999)999-9999]"}
        ))

        # Custom validations
        def clean(self):

            # Get cleaned version of password, confirmation, & username
            username = self.cleaned_data.get("usernameSubmit")
            password = self.cleaned_data.get("passwordSubmit")
            confirmation = self.cleaned_data.get("confirmationSubmit")

            # See if username already exists
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("User already exists")

            # Validate password & confirmation match
            if password != confirmation:
                raise forms.ValidationError("Passwords must match")

    if request.method == "POST":

        # Obtain user submitted phone from form
        form = registerForm(request.POST)

        # Server-side check for form validity
        if form.is_valid():

            # Isolate registerForm cleaned data
            username = form.cleaned_data.get("usernameSubmit")
            firstname = form.cleaned_data.get("firstnameSubmit")
            lastname = form.cleaned_data.get("lastnameSubmit")
            email = form.cleaned_data.get("emailSubmit")
            password = form.cleaned_data.get("passwordSubmit")
            phone = form.cleaned_data["phoneSubmit"]

            # Attempt to create new user
            try:
                user = User.objects.create_user(username, email, password)
                user.first_name = firstname
                user.last_name = lastname
                user.Phone = phone.as_e164
                user.save()

            # If error occurs delete user object . . .
            except:
                if User.objects.filter(username=username).exists():
                    user.delete()
                
                # And render `register.html` with error message
                return render(request, "riverRent/register.html", {
                    "form": form,
                    "message": "Server error has occurred. Contact your administrator.",
                })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        
    # If GET, create blank form for phone, & return `register.html`
    else:
        form = registerForm()
        
    return render(request, "riverRent/register.html", {
        "form": form,
    })


# HTTP methods decorator
@require_http_methods(["GET"])
def category(request, tripCategory):

    trips = Trip_Detail.objects.filter(Trip_Category = tripCategory)

    return render(request, "riverRent/category.html", {
        "trips": trips,
    })


# HTTP methods decorator
@require_http_methods(["GET"])
def trip(request, tripSelection):

    tripDetails = Trip_Detail.objects.get(Trip_Number = tripSelection)
    tripPackages = Trip_Package.objects.filter(Trip = tripDetails)

    return render(request, "riverRent/trip.html", {
        "tripDetails": tripDetails,
        "tripPackages": tripPackages,
    })


# HTTP methods decorator
@require_http_methods(["POST"])
def avail(request, tripSelection):

    # User reached view via Ajax POST attempt to get availability
    if request.is_ajax and request.method == "POST":

        # Try to obtain POST data and determine boats available for trip
        try:

            # Get trip details for selected trip
            tripDetails = Trip_Detail.objects.filter(Trip_Number = tripSelection)

            # Get all trip packages
            allTripPackages = Trip_Package.objects.all()
            
            # Obtain trip packages available for tripSelection
            tripPackages = allTripPackages.filter(Trip__in=tripDetails)

            # Get selectedDate & convert to dateTime format
            rawSelectedDate = json.loads(request.body)['selectedDate']
            selectedDate = timezone('US/Eastern').localize(
                datetime.strptime(rawSelectedDate, '%a %b %d %Y'))

            # Get invoice lines for selectedDate
            currDayInvLines = Invoice_Line.objects.filter(Arrival__date=selectedDate.date())
            
            # Get boats available data for given trip
            boatAvail = Water_Craft.objects.filter(trip_package_boats__in=tripPackages)

            # Interate through invoice lines to get water craft type
            for invLine in currDayInvLines:
                invWaterCraftId = allTripPackages.get(id=invLine.Selected_Trip_Package_id).Water_Craft_Type_id
    
                # Iterate through boatAvail & change count for matches
                for boat in boatAvail:
                    if boat.id == invWaterCraftId:
                        boat.Count = boat.Count - invLine.Quantity


            # Serialize tripPackages & boatAvail data to JSON & return
            tripPackagesJson = serialize("json", tripPackages)
            boatAvailJson = serialize("json", boatAvail)
            tripDetailsJson = serialize("json", tripDetails)
            return JsonResponse({'status': 200, 'tripPackagesJson': tripPackagesJson
                , 'boatAvailJson': boatAvailJson, 'tripDetailsJson': tripDetailsJson})

        # Return server error for any fails
        except:
            return JsonResponse({'status': 500})


# HTTP methods decorator
@require_http_methods(["GET", "POST"])
def cart(request):

    # User reached view via AJAX POST (attempt to submit new order from cart)
    if request.is_ajax and request.method == "POST":

        # Try to process POST
        try:
        
            # Get userShopping cart from POST body
            userShoppingCart = json.loads(request.body)['userShoppingCart']

            # Get trip packages
            tripPackages = Trip_Package.objects.all()

            # Get boats available data
            boatAvail = Water_Craft.objects.all()

            # Iterate through userShoppingCart            
            for item in userShoppingCart:
                
                # Construct raw date string from POST
                rawDate = item['selectedDate'] + " " + item['selectedTime']
                selectedDate = timezone('US/Eastern').localize(datetime.strptime(
                    rawDate, '%a %b %d %Y %I:%M:%S %p'))

                # Iterate through boatsSelected
                for boat in item['boatsSelected']:
                    
                    # Get boat quantity, & trip package selection
                    boatQuan = item['boatsSelected'][boat]
                    selectedPackage = Trip_Package.objects.get(Water_Craft_Type=boat
                        , Trip=Trip_Detail.objects.get(Trip_Number=item['tripSelection']))
                    
                    # if not already created, get user data & create new invoice
                    if 'currInvoice' not in locals():
                        currUser = User.objects.get(username=userShoppingCart[0]['userName'])
                        currInvoice = Invoice(Customer=currUser)
                        currInvoice.save()

                    # Get invoice lines for selectedDate
                    currDayInvLines = Invoice_Line.objects.filter(Arrival__date=selectedDate.date())

                    # Interate through invoice lines to get water craft type
                    for invLine in currDayInvLines:
                        invWaterCraftId = tripPackages.get(
                            id=invLine.Selected_Trip_Package_id).Water_Craft_Type_id

                        # If inv line boat same as boat =, && boat.Count == 0 . . .
                        if ((boatAvail[int(boat) - 1].id == invWaterCraftId) and (
                                boatAvail[int(boat) - 1].Count - invLine.Quantity == 0)):
                        
                            # Delete current invoice, & send alert that quantity is now 0
                            currInvoice.delete()
                            errMessage = f'{boatAvail[int(boat) - 1].Type} is currently out of ' \
                                'stock for ' + item['selectedDate'] +'. Invoice has been backed ' \
                                'out. Please delete cart item that matches this, then select ' \
                                'different date, or boat.'
                            return JsonResponse({'status': 403, 'errMessage': errMessage})
                
        
                    # Create invoice lines for invoice
                    invoiceLine = Invoice_Line(Quantity=boatQuan, Arrival=selectedDate, On_Invoice=currInvoice
                        , Selected_Trip_Package=selectedPackage)
                    invoiceLine.save()
        
            # On success, return 200 status
            return JsonResponse({'status': 200})

        # Return server error for any fails
        except:
            return JsonResponse({'status': 500})

    # User reached view via GET (user requesting shopping cart list)
    else:

        # Get all boats available data & serialize
        boatAvail = Water_Craft.objects.all()
        boatAvailJson = serialize("json", boatAvail)

        context = {"boatAvailJson": boatAvailJson}

        return render(request, "riverRent/cart.html", context)

