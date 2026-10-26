

import {carts, removeItemFromCart, updateDeliveryOption} from  '../../data/carts.js';
import {products} from  '../../data/products.js';
import {formatCurrency} from '../utils/money.js';
import {deliveryOptions} from '../../data/deliveryOption.js';
import dayjs from 'https://unpkg.com/supersimpledev@8.5.0/dayjs/esm/index.js';



export function renderCheckoutPage() {

  let checkoutElementHTML = '';
  carts.forEach((cartItems) => {

  const productId = cartItems.productId;
  let matchingProduct;


  products.forEach((productItems) => {
   
  
    if(productId === productItems.id) {
      matchingProduct =  productItems;
  }
  });
  
// step7: so <div class="delivery-date"> Delivery date: Tuesday, June 21 </div> here based on the delivery option we choose in cart  we need to update the delivery date as well which is above to handle that we are getting the cart delivery option id then we are looping the deliveryoptions array and match with cart deliveryoption id if matched we are getting that complete object inside the array based on that we are formating above date we are updating dateSting to Delivery date: Tuesday, June 21

  const deliveryOptionId = cartItems.deliveryOptionId;
  let deliveryOption;
  deliveryOptions.forEach((option) => {
    if (option.id === deliveryOptionId) {
      deliveryOption = option;
    }

  });
  const today = dayjs();
  const deliveryDate = today.add(deliveryOption.deliveryDays, 'days');
  const dateSting = deliveryDate.format('dddd, MMMM D')


  checkoutElementHTML += `
                            <div class="cart-item-container js-cart-item-container-${cartItems.productId} js-cart-item-container">
                              <div class="delivery-date">
                                Delivery date: ${dateSting}
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
                                  <div class="product-quantity js-product-quantity-${cartItems.productId}">
                                    <span>
                                      Quantity: <span class="quantity-label">${cartItems.quantity}</span>
                                    </span>
                                    <span class="update-quantity-link link-primary">
                                      Update
                                    </span>
                                    <span class="delete-quantity-link link-primary js-delete-quantity js-delete-quantity-${cartItems.productId}" data-product-id="${cartItems.productId}">
                                      Delete
                                    </span>
                                  </div>
                                </div>
                                <div class="delivery-options">
                                  <div class="delivery-options-title">
                                    Choose a delivery option:
                                  </div>
                                ${deliveryOptionHTML(cartItems.productId, cartItems)}
                              </div>
                            </div>
                          </div>

                          `
});


//Step4: Creating the html for delivery-options. using one delivery options html we are going to use the loop and iterate and create a 3 delivery options based on the data we have it in deliveryOptions array, so we are commenting the above static delivery option html and generating dynamic. We are going to create this as function and going to pass above checkoutElementHTML, that is the place it has delivery-options, so there we will remove the html code.

function deliveryOptionHTML(matchingProduct, cartItems) {
  let html = '';

  deliveryOptions.forEach((deliveryOption) => {
      //Step5: here with one delivery option html we are going create 3 html using the data with array. So we need to pass the date based on the current date. so using dayjs library we are going to genrate it. So here we are generating the current date and based on that we are subsituting below, on terinary operator if deliveryOption.priceCents === 0 the it should be free else $9.99 - Shipping inorder to format like this we used terinary operator, need to create html for all 3 delivery options appending as well and calling the function above as well. This line is part of the function do passing this as parameter ( name="delivery-option-${cartItems.productId}">)

    const today = dayjs();
    const deliveryDate = today.add(deliveryOption.deliveryDays, 'days');
    const dateSting = deliveryDate.format('dddd, MMMM D')
  
 

    const priceString = deliveryOption.priceCents === 0 ? 'FREE' : `$${formatCurrency(deliveryOption.priceCents)} -`;
//Step6: currently we have given like this so for each product the 3 option will be checked by default <input type="radio" checked but we have to make sure based on the cart deliverOptionId the deliveryoption in UI must be checked. to handle that we are writng below and updating this line <input type="radio" checked, if isChecked true then checked else empty and in thsi function we dont have cartItems so we are just passing cartItems in the function and where we call this function have access to cartItems paremter so calling place also we are passing this

    const isChecked  = deliveryOption.id === cartItems.deliveryOptionId;




    html += ` <div class="delivery-option js-delivery-option"
                data-product-id="${matchingProduct}" 
                data-delivery-option-id="${deliveryOption.id}"> 

                  <input type="radio" ${ isChecked ? 'checked' : ''}
                    class="delivery-option-input"
                    name="delivery-option-${matchingProduct}">
                  <div>
                    <div class="delivery-option-date">
                      ${dateSting}
                    </div>
                    <div class="delivery-option-price">
                      ${priceString} Shipping
                    </div>
                  </div>
                </div>
            `

  });


  return html;

}

document.querySelector('.js-order-summary').innerHTML = checkoutElementHTML;



document.querySelectorAll('.js-delete-quantity')
  .forEach((deleteItems) => {
    deleteItems.addEventListener('click', () => {
      const productId = deleteItems.dataset.productId;
      
      removeItemFromCart(productId);
      
      const conatiner = document.querySelector(`.js-cart-item-container-${productId}`);
  
      conatiner.remove();
      //step12: same we apply for remove as well  ie delete the product from cart
      renderCheckoutPage();
      
    })
  });

//step9: so using dom when the element is clicked we are updating the delivery dates and option for that we are adding the class here <div class="delivery-option">. so when delivery option is clicked it run the function, for that we need to pass 2 parameter, that we are getting using data attribute so here <div class="delivery-option js-delivery-option">we are adding data attribute then using shorthand property we are getting that

document.querySelectorAll('.js-delivery-option')
  .forEach((element) => {
    element.addEventListener('click', () => {
      const {productId, deliveryOptionId} = element.dataset;
      console.log(productId);
      console.log(deliveryOptionId);

      updateDeliveryOption(productId, deliveryOptionId);
      //step11: after update we are rendering the page, so the update will be in realtime
      renderCheckoutPage();

    })

  });

}