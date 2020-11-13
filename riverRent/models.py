# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser

# Python imports
from datetime import datetime
from pytz import timezone

# Third party imports
from phonenumber_field.modelfields import PhoneNumberField


# Model from AbstractUser for customers
class User(AbstractUser):
    Phone = PhoneNumberField(null=False, blank=False)


# Model for river trip details
class Trip_Detail(models.Model):
    Trip_Number = models.CharField(max_length=3)
    Trip_Category = models.CharField(max_length=10)
    Put_In = models.CharField(max_length=64)
    Take_Out = models.CharField(max_length=64)
    Distance = models.DecimalField(max_digits=4, decimal_places=1)
    Time_Desc = models.CharField(max_length=40)
    Final_Start_Time = models.TimeField()
    Description = models.CharField(max_length=1024)
    Level = models.CharField(max_length=40)

    # Define admin display return format
    def __str__(self):
        return f"Trip {self.Trip_Number}"


# Model for Water Craft inventory
class Water_Craft(models.Model):
    Type = models.CharField(max_length=40)
    Count = models.PositiveSmallIntegerField()

    # Define admin display return format
    def __str__(self):
        return f"{self.Type} / Count: {self.Count}"


# Model for Trip Packages
class Trip_Package(models.Model):
    Water_Craft_Type = models.ForeignKey(
        Water_Craft, on_delete=models.CASCADE, related_name="trip_package_boats")
    Trip = models.ForeignKey(
        Trip_Detail, on_delete=models.CASCADE, related_name="trip_packages")
    Price = models.DecimalField(max_digits=7, decimal_places=2)

    # Define admin display return format
    def __str__(self):

        # Strip just water craft type for display here
        waterCraft = f"{self.Water_Craft_Type}".split("/")[0]
        return f"{self.Trip} with {waterCraft} for ${self.Price}"


# Model for invoices
class Invoice(models.Model):
    Invoice_Number = models.AutoField(primary_key=True)
    Customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_invoices")

    # Define admin display return format
    def __str__(self):
        return f"Invoice #{self.Invoice_Number} for {self.Customer}"


# Model for invoice lines
class Invoice_Line(models.Model):
    On_Invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="invoice_lines")
    Quantity = models.PositiveSmallIntegerField()
    Selected_Trip_Package = models.ForeignKey(
        Trip_Package, on_delete=models.CASCADE, related_name="package_invoice_lines")
    Arrival = models.DateTimeField()

    # Define admin display return format
    def __str__(self):

        # Obtain arrival datetime object & make local text format
        arrTimeRaw = f"{self.Arrival}"
        arrTime = datetime.strptime(arrTimeRaw, '%Y-%m-%d %H:%M:%S%z')
        localArrTime = arrTime.astimezone(timezone('US/Eastern'))
        arrTimeTxt = localArrTime.strftime("%a %b %d at %I:%M %p")
        
        return f"{self.On_Invoice} - {self.Selected_Trip_Package}, Qty: {self.Quantity}, Arrival: {arrTimeTxt}"

