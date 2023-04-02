document.addEventListener("DOMContentLoaded", function() {
    // Test to see if anything is already stored in localStorage
    console.log(localStorage.getItem("cart"));
    
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener("click", addToCart);
        console.log("ADD-TO-CART BUTTON EVENT LISTENER ADDED");
    });

    const viewCartButton = document.getElementById("view-cart-button");
    viewCartButton.addEventListener("click", updateCartText)
    
});

function updateCartText() {
    const cartDiv = document.getElementById("cart-view");
    cartDiv.innerText = localStorage.getItem("cart");
}

function addToCart(event) {
    const productName = event.target.parentNode.querySelector("span").textContent;
    const productPrice = parseFloat(event.target.parentNode.querySelector("h4").textContent.slice(1));
    const productQuantity = parseInt(event.target.parentNode.querySelector("input").value);
  
    console.log("ADD TO CART PRESSED!!!!");

  // Create an object to represent the product
    const product = {
        name: productName,
        price: productPrice,
        quantity: productQuantity
    };
    
    // Get the shopping cart from localStorage or create a new one
    let cart = JSON.parse(localStorage.getItem("cart")) || {};
    
    // Add the product to the shopping cart
    if (cart[productName]) {
        cart[productName].quantity += productQuantity;
    } else {
        cart[productName] = product;
    }
    
    // Save the shopping cart to localStorage
    localStorage.setItem("cart", JSON.stringify(cart));
}

