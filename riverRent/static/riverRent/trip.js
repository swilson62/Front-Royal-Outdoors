// Global variables
var fp = ""; // Var for flatpickr calendar instance
var timeFp = ""; // Var for flatpickr time instance
var boatsSelected = {};
var boatsAvail = {};
var tripPackages = {};
var priceTotal = 0;
var selectedDate = "";
var tripSelection = "";
var selectedTime = "07:00:00 AM";
var tripDetailsJson = [];
var maxTimeAvail = "";


// subtractSelection click logic
function subtractSelection(waterCraftTypeId) {

    // Get current count from innerHTML, subtract one, & set innerHTML to new value
    let count = parseInt(document.getElementById(`selectionCount${waterCraftTypeId}`).innerHTML);
    count --;
    boatsSelected[waterCraftTypeId] = count;
    document.getElementById(`selectionCount${waterCraftTypeId}`).innerHTML = `${count}`

    // If Boats Available count exists, add one to it
    if (document.getElementById(`availCount${waterCraftTypeId}`).innerHTML != "") {
        r = parseInt(document.getElementById(`availCount${waterCraftTypeId}`).innerHTML);
        boatsAvail[waterCraftTypeId] = boatsAvail[waterCraftTypeId] + 1;
        
        // Build availCount DOM
        document.getElementById(`availCount${waterCraftTypeId}`).innerHTML = `
            <span class="largeViewport">Boats </span>Available: ${boatsAvail[waterCraftTypeId]}`;
    } 

    // If Boats Available count > 0, enable add link
    if (boatsAvail[waterCraftTypeId] > 0) {
        document.getElementById(`addSelection${waterCraftTypeId}`).style.pointerEvents = "auto";
        document.getElementById(`addSelection${waterCraftTypeId}`).style.color = "orange";
    }

    // If count > 0, enable subtract link, and . . .
    if (count > 0) {
        document.getElementById(`subtractSelection${
            waterCraftTypeId}`).style.pointerEvents = "auto";
        document.getElementById(`subtractSelection${waterCraftTypeId}`).style.color = "orange";

        // Build calendarDOM, and  . . .
        document.getElementById('calendarHdr').innerHTML = 'Select Rental Date:';
        buildCalDOM();

        // Provided date has been selected, & priceTotal has been calculated . . .
        // if (priceTotal != 0) {   # Original check that caused bug after later bug fix
        if (selectedDate != "") {
        
            // Call function to build time DOM 
            buildTimeDom();
            
            // Call function to calculate priceTotal & build related DOM
            calcPriceTotal();
        }

    // Else disable subtract link
    } else {
        document.getElementById(`subtractSelection${
            waterCraftTypeId}`).style.pointerEvents = "none";
        document.getElementById(`subtractSelection${waterCraftTypeId}`).style.color = "grey";

        // Determine if all boatCounts are now at 0  . . .
        boatCounts = document.getElementsByClassName('boatCount');

        var boatCountsArr = [];
        for (x = 0; x < boatCounts.length; x++) {
            boatCountsArr.push(boatCounts[x].innerHTML);
        }

        function boatCountZero(boatCount) {
            return boatCount === "0";
        }
        
        // . . . and if so tear down calendar
        if (boatCountsArr.every(boatCountZero)) {
            completeTearDown();
        
        // Else call buildTimeDom() in case maxTimeAvail needs reset for tube de-selection
        } else {
            buildTimeDom();

        // And call function to calculate priceTotal & build related DOM
            calcPriceTotal();
        }
    }
}


// addSelection click logic
function addSelection(waterCraftTypeId) {
    
    // Get current count from innerHTML, add one, & set innerHTML to new value
    var count = parseInt(document.getElementById(`selectionCount${waterCraftTypeId}`).innerHTML);
    count ++;
    boatsSelected[waterCraftTypeId] = count;
    document.getElementById(`selectionCount${waterCraftTypeId}`).innerHTML = `${count}`;

    // If Boats Available count exists, subtract one from it
    if (document.getElementById(`availCount${waterCraftTypeId}`).innerHTML != "") {
        r = parseInt(document.getElementById(`availCount${waterCraftTypeId}`).innerHTML);
        boatsAvail[waterCraftTypeId] = boatsAvail[waterCraftTypeId] - 1;
        
        // Build availCount DOM
        document.getElementById(`availCount${waterCraftTypeId}`).innerHTML = `
            <span class="largeViewport">Boats </span>Available: ${boatsAvail[waterCraftTypeId]}`;
    }

    // If Boats Available count reaches 0, disable add link
    if (boatsAvail[waterCraftTypeId] === 0) {
        document.getElementById(`addSelection${waterCraftTypeId}`).style.pointerEvents = "none";
        document.getElementById(`addSelection${waterCraftTypeId}`).style.color = "grey";
    }

    // Enable subtract link in case it is disabled
    document.getElementById(`subtractSelection${waterCraftTypeId}`).style.pointerEvents = "auto";
    document.getElementById(`subtractSelection${waterCraftTypeId}`).style.color = "orange";

    // Build calendarDOM
    document.getElementById('calendarHdr').innerHTML = 'Select Rental Date:';
    buildCalDOM();

    // Provided date has been selected, & priceTotal has been calculated . . .
    if (selectedDate!= "" && priceTotal != 0) {

        // Call function to build time DOM 
        buildTimeDom();

        // Call function to calculate priceTotal & build related DOM
        calcPriceTotal();
    }
}


// Function to build flatpickr calendar instance DOM
function buildCalDOM() {
    fp = flatpickr('#calendarDOM', {
        inline: true,
        dateFormat: "Y-m-d",
        disable: [
            {
                from: "2020-12-02",
                to: "2021-03-13"
            },
        ],
        minDate: new Date().fp_incr(1),     // > Tomorrow
        maxDate: "2021-11-02",
        onChange: function(rawSelectedDate) {
            dateSelected(rawSelectedDate);
        },
    });
}


// Function to build time header and flatpickr time DOM
function buildTimeDom() {

    // If boatsSelected includes tubes, set max time to 12 PM
    if (Object.keys(boatsSelected).includes("8") && boatsSelected[8] > 0) {
        maxTimeAvail = "12:00:00";

        // If selectedTime > 12PM, reset
        if (selectedTime > "12:00:00 PM") {
            timeFp.setDate("12:00:00 PM");
            selectedTime = "12:00:00 PM"
            alert(`Selected time was greater than final allowed arrival time for trips with tubes.
                 Time has been adjusted to maximum allowed arrival time.`)
        }

    // Else set to Final_Start_Time from DB
    } else {
        maxTimeAvail = tripDetailsJson[0].fields.Final_Start_Time;
    }

    // Time header
    document.getElementById('timeHdr').innerHTML = 
        `<div style="margin-top: 20px;"></div><span class="h6">Select Shuttle Time:</span>
        <span id="infoTooltip" tabindex="0"><a href="#" class="fas fa-info-circle" id="infoIcon">
        </i></span>`

    // Time header tooltip config
    $('#infoTooltip').tooltip({
        trigger: 'hover focus',
        title: 'First shuttle 7AM. Shuttles leave every 30 min. Final available shuttle depends \
on trip selected. Times are recommendations only. Shuttles are first come first serve. Arrivals \
after final available shuttle time, RISK SERVICE DENIAL.',
    })
    

    // flatpickr timeDOM
    timeFp = flatpickr('#timeDom', {
        inline: true,
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        defaultHour: 07,
        defaultMinute: 00,
        minuteIncrement: 30,
        minTime: "07:00",
        maxTime: maxTimeAvail,
        onChange: function(rawSelectedTime) {
            selectedTime = new Date(rawSelectedTime.toString()).toLocaleTimeString();
        },
    })
}


function dateSelected(rawSelectedDate) {
    // Obtain selectedDate passed by calendar & tripSelection from path
    selectedDate = new Date(rawSelectedDate.toString()).toDateString();
    tripSelection = window.location.pathname.split("/")[2];
    
    if (selectedDate.toString() != "Invalid Date") {
        fetch(`/avail/${tripSelection}`, {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "X-CSRFtoken": getCookie('csrftoken'),
                "Content-Type": "application/json;charset=utf-8",
            },
            body: JSON.stringify({ "selectedDate": selectedDate })
        })
    
        // Convert response into JSON data
        .then(response => response.json())
    
        // If returned status === 200 . . .
        .then(data => {
    
            // If status OK . . .
            if (data.status === 200) {
                
                // Get tripPackaesJson & boatAvailJson from data
                tripPackagesJson = JSON.parse(data.tripPackagesJson);
                boatAvailJson = JSON.parse(data.boatAvailJson);
                tripDetailsJson = JSON.parse(data.tripDetailsJson);
                
                // Iterate through boatAvailJson to build object with {pk: count}
                for (r = 0; r < boatAvailJson.length; r++) {
                    boatsAvail[boatAvailJson[r].pk] = boatAvailJson[r].fields.Count;
                }

                // Iterate through tripPackagesJson to build object with {Water_craft_Type: Price}
                for (q = 0; q < tripPackagesJson.length; q++) {
                    tripPackages[tripPackagesJson[
                        q].fields.Water_Craft_Type] = tripPackagesJson[q].fields.Price;
                }

                // If users shopping cart exists get it
                if (localStorage.getItem(`${currentUser}_shoppingCart`) != null) {
                    shoppingCart = JSON.parse(localStorage.getItem(`${currentUser}_shoppingCart`));

                    // Iterate through shopping cart
                    for (item in shoppingCart) {

                        // Iterate through cart boatsSelected
                        for (boat in shoppingCart[item].boatsSelected) {

                            // Subtract boats in cart from boatsAvail
                            boatsAvail[boat] = boatsAvail[
                                boat] - shoppingCart[item].boatsSelected[boat]
                        }
                    }
                }

                // Loop through boatsAvail object, and . . .
                for (boat in boatsAvail) {
                    
                    // Get object name
                    z = parseInt(boat);
                    
                    // If avail === 0 . . .
                    if (boatsAvail[z] === 0) {

                        // And if boatsSelected matching current boat > 0, delete
                        if (boatsSelected[z] > 0) {
                            delete boatsSelected[z];
                            alert('Boat selected no longer available for date selected.')
                        }

                        // And if subtract enabled, disable
                        if (document.getElementById(
                            `subtractSelection${z}`).style.pointerEvents === "auto") {
                                document.getElementById(
                                    `subtractSelection${z}`).style.pointerEvents = "none";
                                document.getElementById(`subtractSelection${z}`).style.color = "grey";
                            }
                        
                        // Disable add button
                        document.getElementById(
                            `addSelection${z}`).style.pointerEvents = "none";
                        document.getElementById(`addSelection${z}`).style.color = "grey";

                        // Set selectionCount innerHTML to 0
                        document.getElementById(`selectionCount${z}`).innerHTML = "0";

                        // Determine if all boatCounts are now at 0  . . .
                        boatCounts = document.getElementsByClassName('boatCount');

                        var boatCountsArr = [];
                        for (x = 0; x < boatCounts.length; x++) {
                            boatCountsArr.push(boatCounts[x].innerHTML);
                        }
                        
                        function boatCountZero(boatCount) {
                            return boatCount === "0";
                        }
                            
                        // . . . and if so tear down calendar
                        if (boatCountsArr.every(boatCountZero)) {
                            completeTearDown();
                        }
                    
                    // Else if != 0, and . . .
                    } else {

                        // has been disabled, re-enable add button
                        if (document.getElementById(
                            `addSelection${z}`).style.pointerEvents === "none") {
                            document.getElementById(
                                `addSelection${z}`).style.pointerEvents = "auto";
                            document.getElementById(`addSelection${z}`).style.color = "orange";
                        }
                    }
                        
                    // If boatSelected matching that name exists . . .
                    if (boatsSelected[z]) {
                        
                        // If avail > 0 subtract selected from avail
                        if (boatsAvail[z] - boatsSelected[z] > 0) {
                            boatsAvail[z] = boatsAvail[z] - boatsSelected[z];

                        // Else if avail - selected === 0, make avail 0, & disable add button
                        } else if (boatsAvail[z] - boatsSelected[z] === 0) {
                            document.getElementById(`selectionCount${z}`).innerHTML = `${
                                boatsAvail[z]}`;
                                boatsSelected[z] = boatsAvail[z];
                                boatsAvail[z] = 0;
                                document.getElementById(
                                    `addSelection${z}`).style.pointerEvents = "none";
                                document.getElementById(`addSelection${z}`).style.color = "grey";
                        
                        // Else throw err, adjust value to max, & disable add link
                        } else {
                            alert('Selection count exceeds Max. Has been adjusted.');
                            document.getElementById(`selectionCount${z}`).innerHTML = `${
                                boatsAvail[z]}`;
                            boatsSelected[z] = boatsAvail[z];
                            boatsAvail[z] = 0;
                            document.getElementById(
                                `addSelection${z}`).style.pointerEvents = "none";
                            document.getElementById(`addSelection${z}`).style.color = "grey";
                        }
                    }

                    // Build availCount DOM
                    if (selectedDate != "") {
                        document.getElementById(`availCount${z}`).innerHTML = `
                        <span class="largeViewport">Boats </span>Available: ${boatsAvail[z]}`;
                    }
                }
                
                // If selectedDate is still populated
                if (selectedDate != "") {
                    // Call function to build time DOM
                    buildTimeDom()

                    // Call function to calculate priceTotal & build related DOM
                    calcPriceTotal();
                } 

            // Else throw server error
            } else {
                alert("Internal Server Error");
            }
        })
    }
}


// Function to calculate priceTotal & build priceTotal DOM
function calcPriceTotal() {
    
    // Start by zeroing priceTotal
    priceTotal = 0;
    
    // Iterate through boatsSelected to calculate priceTotal
    for (boat in boatsSelected) {
        priceTotal += boatsSelected[parseInt(boat)] * parseInt(tripPackages[
            parseInt(boat)]);
    }
    
    // Build priceTotalDom
    document.getElementById('priceTotalDom').innerHTML = `<div style="margin-top: 20px;"></div>
        <h6>Price Total: $${priceTotal}</h6>`;
}


// Function used to get csrf cookie (see https://docs.djangoproject.com/en/3.1/ref/csrf/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// Function called by Cancel or `X` click (and other things)
function completeTearDown() {
    
    // Tear down fp instance if one exists
    if (fp != "") {
        fp.clear();
        fp.destroy();
        
        // Tear down timeFp instance if one exists
        if (timeFp != "") {
            timeFp.clear();
            timeFp.destroy();
        }
    }
    
    // Remove calendar header
    document.getElementById('calendarHdr').innerHTML = '';
    
    // If date has not been selected yet, 0 out selectionCount DOM items
    if (Object.keys(boatsAvail).length === 0) {
        for (boat in boatsSelected) {
            e = parseInt(boat);
            document.getElementById(`selectionCount${e}`).innerHTML = "0";
        }

    } else {
        // Tear down boat availability list, selectionCount DOM items and . . .
        for (boat in boatsAvail) {
            w = parseInt(boat);
            document.getElementById(`availCount${w}`).innerHTML = "";
            document.getElementById(`selectionCount${w}`).innerHTML = "0";
        }
    } 

    // Reset all global vars to initial values
    fp = ""; // Var for flatpickr calendar instance
    timeFp = ""; // Var for flatpickr time instance
    boatsSelected = {};
    boatsAvail = {};
    tripPackages = {};
    priceTotal = 0;
    selectedDate = "";
    tripSelection = "";
    selectedTime = "07:00:00 AM";
    tripDetailsJson = [];
    
    // Remove priceTotalDom, timeHdr, & timeDom
    document.getElementById('priceTotalDom').innerHTML = "";
    document.getElementById('timeHdr').innerHTML = "";
    document.getElementById('timeDom').innerHTML = "";

    // Disable all subtract buttons
    subtractButtons = document.getElementsByClassName('subtractSelections');
    for (i = 0; i < subtractButtons.length; i++) {
        subtractButtons[i].style.pointerEvents = "none";
        subtractButtons[i].style.color = "grey";
    }

    // Enable all add buttons
    addButtons = document.getElementsByClassName('addSelections');
    for (i = 0; i < addButtons.length; i++) {
        addButtons[i].style.pointerEvents = "auto";
        addButtons[i].style.color = "orange";
    }
}


// Function called by click on addToCart button
function addToCart() {

    // Declare local var orders
    let orders = [];

    // If no boats selected, send alert
    if (Object.keys(boatsSelected).length == 0) {
        alert("Please Select Some Boats");
    
    // Else if not date selected, send alert
    } else if (selectedDate === "") {
        alert("Please Select a Date");
    
    // Else store cart in local storage
    } else {

        // Set newOrder var as an array of object containing order data
        let newOrder = {"userName": currentUser, "selectedDate": selectedDate
            , "tripSelection": tripSelection, "selectedTime": selectedTime
            , "boatsSelected": boatsSelected, "priceTotal": priceTotal};

        // If no previous orders, add new order to local storage
        if (localStorage.getItem(`${currentUser}_shoppingCart`) == null || localStorage.getItem(
            `${currentUser}_shoppingCart`) == "[]") {
            
            // Push newOrder object onto orders array
            orders.push(newOrder);

            // Store locally array of objects as ShoppingCart
            localStorage.setItem(`${currentUser}_shoppingCart`, JSON.stringify(orders));

            // Update cart count
            updateCartItemNum();

            // Notify user
            alert('Item has been added to cart. Sales are not final until check out succeeds. \
Availability changes often, and sale will fail if boats are not available. Please check out ASAP!');

            // Tear everything down
            completeTearDown();
            $('#bookABoat').modal('hide');
        
        // Else if previous orders exist
        } else {

            // Obtain old orders, push latest, & store locally
            orders = JSON.parse(localStorage.getItem(`${currentUser}_shoppingCart`));
            orders.push(newOrder);
            localStorage.setItem(`${currentUser}_shoppingCart`, JSON.stringify(orders));

            // Update cart count
            updateCartItemNum();

            // Notify user
            alert('Item has been added to cart. Sales are not final until check out succeeds. \
Availability changes often, and sale will fail if boats are not available. Please check out ASAP!');

            // Tear everything down
            completeTearDown();
            $('#bookABoat').modal('hide');
        }
    }
}


// Function called to update cart count
function updateCartItemNum() {

    // Get current cart totalItemsNum
    totalItems = parseInt(document.getElementById("totalItemsNum").innerHTML);

    // Update cart count & count display innerHTML
    totalItems = totalItems + 1;
    document.getElementById("totalItemsNum").innerHTML = `${totalItems}`;
}



document.addEventListener('DOMContentLoaded', () => {

    // Disable subtract link on initial load
    subtractButtons = document.getElementsByClassName('subtractSelections');
    for (i = 0; i < subtractButtons.length; i++) {
        subtractButtons[i].style.pointerEvents = "none";
        subtractButtons[i].style.color = "grey";
    }

    // When Cancel  or 'X' is clicked run completeTearDown()
    document.getElementById('modalCancel').addEventListener('click', completeTearDown);
    document.getElementById('modalExit').addEventListener('click', completeTearDown);

    // When addToCart button is clicked, run addToCart()
    document.getElementById('addToCart').addEventListener('click', addToCart);
})
