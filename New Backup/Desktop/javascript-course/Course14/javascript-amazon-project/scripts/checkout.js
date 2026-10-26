//Step8: on the file we are going to dynamically create a html page based on the data we have in cart. but we are assuming we have 2 data in carts now and going to have that in data and based on that data we are going to generate the html and then going to make it interactive. so till now our carts will have object inside we have 2 attribut, productid and quantity, the same we are going to create here. We can directly use the carts array and work, but for learning we are going to have that array created ie creating the data then generate the html. so on the carts.js we are going the inputthe data

//step10: currently our cart has product id and quantity but below in the checkout page it has other details as well like product name, price and product image. so now we are going to use the product id and going to fetch the name, imahe and price. And we are dynamically generating the html for the product we have it our cart. So our cart now has 2 prodcut , so using that we are going to generate the html page for checkout ie generating the items which in the cart

//step11: importing the carts array here using module

import {carts, removeItemFromCart} from  '../data/carts.js';
import {products} from  '../data/products.js';
import {formatCurrency} from './utils/money.js';

//Step11 iterating the carts and comparing with the products array so if the product id in carts matcchs with prducts array then we can get the corresponding image, name and price from products array. Then using the template string we can generate the html element for the data in cart.

let checkoutElementHTML = '';
carts.forEach((cartItems) => {
  //step12: getting the product id from the cart
  const productId = cartItems.productId;
  let matchingProduct;

// step13: iterating the products, so we are comparing the the cart product id with product product id, if it matched then we are saving that to product details to matchingproduct
  products.forEach((productItems) => {
   
  
    if(productId === productItems.id) {
      matchingProduct =  productItems;
  }
  });
  
console.log(matchingProduct);
//Step14: generating the html and passing the data as well
  checkoutElementHTML += `
          <div class="cart-item-container js-cart-item-container-${cartItems.productId}">
            <div class="delivery-date">
              Delivery date: Tuesday, June 21
            </div>

            <div class="cart-item-details-grid">
              <img class="product-image"
                src="${matchingProduct.image}">

              <div class="cart-item-details">
                <div class="product-name">
                  ${matchingProduct.name}
                </div>
                <div class="product-price">
                  $${formatCurrency(matchingProduct.priceCents)}
                </div>
                <div class="product-quantity">
                  <span>
                    Quantity: <span class="quantity-label">${cartItems.quantity}</span>
                  </span>
                  <span class="update-quantity-link link-primary">
                    Update
                  </span>
                  <span class="delete-quantity-link link-primary js-delete-quantity" data-product-id="${cartItems.productId}">
                    Delete
                  </span>
                </div>
              </div>

              <div class="delivery-options">
                <div class="delivery-options-title">
                  Choose a delivery option:
                </div>
                <div class="delivery-option">
                  <input type="radio" checked
                    class="delivery-option-input"
                    name="delivery-option-${cartItems.productId}">
                  <div>
                    <div class="delivery-option-date">
                      Tuesday, June 21
                    </div>
                    <div class="delivery-option-price">
                      FREE Shipping
                    </div>
                  </div>
                </div>
                <div class="delivery-option">
                  <input type="radio"
                    class="delivery-option-input"
                    name="delivery-option-${cartItems.productId}">
                  <div>
                    <div class="delivery-option-date">
                      Wednesday, June 15
                    </div>
                    <div class="delivery-option-price">
                      $4.99 - Shipping
                    </div>
                  </div>
                </div>
                <div class="delivery-option">
                  <input type="radio"
                    class="delivery-option-input"
                    name="delivery-option-${cartItems.productId}">
                  <div>
                    <div class="delivery-option-date">
                      Monday, June 13
                    </div>
                    <div class="delivery-option-price">
                      $9.99 - Shipping
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

  `


});

//step16: updating the cart summary page duing dom

document.querySelector('.js-order-summary').innerHTML = checkoutElementHTML;

//step17: as this line " $${(matchingProduct.priceCents / 100).toFixed(2)}" in above template string is repeating code so we are going to create a function for this. As this kind of utility so we are going to create utils folder under script and going top create a js file called money.js as this function is related to money so inside that file we are going to create it. we can create any number of js file based on our requirement and keep the function inside it and updating above and amazon.js file

//step18: on choose deliver option we are using radio button , on radio buttons we have have attribute  name="delivery-option-1", so from our above created template string totally 6 will be there for the first product 3 radio button and second 3 next 3 radio button, please check ui for more details. the problem here is if name is same for all radio button  name="delivery-option-1" like this then only one can select at time, but the problem here is for both the product we can select one button at a time, as the same name is available in both the place. So for each product if we have same radio button name attribute our issue will fix, so on each product out of 3 button we can choose one. so to fix this we are going to pass product id instead of 1 ie  name="delivery-option-1" in this place we have updated like this  name="delivery-option-${cartItems.productId}">

//step19: our next goal is to make it interactive, when we click on delete , we need to delete the product from cart. so using dom we are going to hanlde it so on above template string added class js-delete-quantity on delete button. using queryselector all we are we are taking the delete button, but now using data attribute we are giving the unique info to delete , so using that we can identify which delete we are performing. here we are giving product id to delete, same applying in template string, have added this data-product-id="${cartItems.productId}". then using the dataset getting the product id. So what we do below is getting all delete object and iterating into it, then using addEventListner, if the object is clicked then performing the delete operation, that which delete is clicked is identifying using dataset

document.querySelectorAll('.js-delete-quantity')
  .forEach((deleteItems) => {
    deleteItems.addEventListener('click', () => {
      const productId = deleteItems.dataset.productId;
      //step20 handling the delete operation using the function which is written in carts.js
      removeItemFromCart(productId);
      //step22: now the cart only have the current product ie aftre removeing the product removed, but same need to upodate in UI, so using dom we can do that, so using dom , we can use remove methode and we can remove the element, this is new concept. in order find the element we are going to add the class in the template string that in checkout.js ie js-cart-item-container is the cartitem container so using queryselector we are getting this and will remove, now the problem we dont know as now both the product will have same class, so differentiate it we are going to use the product id like this js-cart-item-container-${cartItems.productId}

      const conatiner = document.querySelector(`.js-cart-item-container-${productId}`);
  //step23: removing using remove method
      conatiner.remove();
      
    })
  });

