document.addEventListener('DOMContentLoaded', () => {

    let totalItems = 0;

    // Set innerHtml of #totalItemNum from # of items in shopping cart if exists
    if (JSON.parse(localStorage.getItem(`${currentUser}_shoppingCart`)) != null) {
        totalItems = JSON.parse(localStorage.getItem(`${currentUser}_shoppingCart`)).length;
    }

    if (userIsAuthenticated = true) {
            document.getElementById("totalItemsNum").innerHTML = `${totalItems}`;
    }
})
