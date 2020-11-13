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


document.addEventListener('DOMContentLoaded', () => {

    // Declare local vars
    let cartPriceTotal = 0;

    // Get user shopping cart
    let userShoppingCart = JSON.parse(localStorage.getItem(`${currentUser}_shoppingCart`));
    
    // Get serialized waterCraft data from json_script template in `cart.html`
    let waterCraft = JSON.parse(JSON.parse(document.getElementById('boatAvailJson').textContent));

    // If shopping cart is empty, redirect to "/".
    if ((userShoppingCart == null) || (userShoppingCart.length == 0)) {
        alert("Shopping cart is empty. Please add items first...")
        window.location.replace("/");

    // Else iterate through userShoppingCart
    } else {
        for (var i = 0; i < userShoppingCart.length; i++) {
            
            // Zero boatList, then build list for this cart item
            let boatList = "";
            for (boat in userShoppingCart[i].boatsSelected) {
                if (parseInt(userShoppingCart[i].boatsSelected[boat]) > 1) {
                    boatList = boatList + `${userShoppingCart[i].boatsSelected[boat]} ${waterCraft[boat - 1].fields.Type}s, `;
                } else {
                    boatList = boatList + `${userShoppingCart[i].boatsSelected[boat]} ${waterCraft[boat - 1].fields.Type}, `;
                }
            }
    
            // Build cart item DOM
            document.getElementById("shoppingCartItemList").innerHTML +=
                `<li><a href="#?itemNum=${i}" class="delCartItem"">&#10060
                ${userShoppingCart[i].selectedDate}: Trip ${userShoppingCart[i].tripSelection}<br>
                Boats: ${boatList}<br>Arrive: ${userShoppingCart[i].selectedTime}&emsp;Price: $${userShoppingCart[i].priceTotal}</a><li><br>`;
    
            cartPriceTotal += parseFloat(`${userShoppingCart[i].priceTotal}`);
        }

    // Create cart price total DOM
    document.getElementById("shoppingCartPriceTotal").innerHTML = `Price Total = $${cartPriceTotal.toFixed(2)}`
    }


    // Function to delete cart items if clicked on
    $(".delCartItem").click(function() {
    
        // Get user shopping cart
        let userShoppingCart = JSON.parse(localStorage.getItem(`${currentUser}_shoppingCart`));
    
        // Get item num to delete
        let itemNum = this.hash.split("=")[1];

        // Delete current users cart
        localStorage.removeItem(`${currentUser}_shoppingCart`);

        // Remove item from currently saved cart array
        userShoppingCart.splice(itemNum, 1);

        // Save currently saved cart array to cart
        localStorage.setItem(`${currentUser}_shoppingCart`, JSON.stringify(userShoppingCart));

        // Reload the page
        location.reload();
    })

    // Function to submit orders when Order button is clicked
    $("#orderButton").click(function() {

        // Get user shopping cart
        let userShoppingCart = JSON.parse(localStorage.getItem(`${currentUser}_shoppingCart`));

        fetch('/cart', {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "X-CSRFtoken": getCookie('csrftoken'),
                "Content-Type": "application/json;charset=utf-8",
            },
            body: JSON.stringify({ "userShoppingCart": userShoppingCart })
        })

        // Convert response into JSON data
        .then(response => response.json())

        // If returned status === 200 . . .
        .then(data => {
    
            // If status OK . . .
            if (data.status === 200) {
                
                // Delete current users cart
                localStorage.removeItem(`${currentUser}_shoppingCart`);

                // Send notification alert & redirect to `/`
                alert ("Order entry has succeeded!")
                location.replace("/")
            
            // Else if error 403 (inventory zeroed) server provided alert
            } else if (data.status === 403) {
                alert(data.errMessage)
            
            // Else throw server error.
            } else {
                alert("Internal Server Error");
            }
        })
    })
})
