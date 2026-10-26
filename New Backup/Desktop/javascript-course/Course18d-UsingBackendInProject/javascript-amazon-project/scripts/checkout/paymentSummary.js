import {carts} from '../../data/carts.js';
import {products} from '../../data/products.js';
import {deliveryOptions} from '../../data/deliveryOption.js';
import {formatCurrency} from '../utils/money.js';
import { addToOrder } from '../../data/orders.js';




export function paymentSummary() {


  
  let productPriceCents = 0;
  let shippingPriceCents = 0;

  carts.forEach((cartItem) => {
    const productId = cartItem.productId;

    let matchingProduct;
    
      products.forEach((productItems) => {
        if(productId === productItems.id) {
          matchingProduct =  productItems;
          productPriceCents += matchingProduct.priceCents * cartItem.quantity;
      }
      });

    

    const deliveryOptionId = cartItem.deliveryOptionId;
    let deliveryOption;
    deliveryOptions.forEach((option) => {
      if (option.id === deliveryOptionId) {
        deliveryOption = option;
        shippingPriceCents += deliveryOption.priceCents;
      }
    
    });
    

  });

 
  const totalBeforeTaxCents = productPriceCents + shippingPriceCents;
  const taxCents = totalBeforeTaxCents * 0.1;
  const totalCents = totalBeforeTaxCents + taxCents;



  const paymentSummaryHTML = `
    <div class="payment-summary-title">
      Order Summary
    </div>

    <div class="payment-summary-row">
      <div>Items (3):</div>
      <div class="payment-summary-money">
        $${formatCurrency(productPriceCents)}
      </div>
    </div>

    <div class="payment-summary-row">
      <div>Shipping &amp; handling:</div>
      <div class="payment-summary-money">
        $${formatCurrency(shippingPriceCents)}
      </div>
    </div>

    <div class="payment-summary-row subtotal-row">
      <div>Total before tax:</div>
      <div class="payment-summary-money">
        $${formatCurrency(totalBeforeTaxCents)}
      </div>
    </div>

    <div class="payment-summary-row">
      <div>Estimated tax (10%):</div>
      <div class="payment-summary-money">
        $${formatCurrency(taxCents)}
      </div>
    </div>

    <div class="payment-summary-row total-row">
      <div>Order total:</div>
      <div class="payment-summary-money">
        $${formatCurrency(totalCents)}
      </div>
    </div>

    <button class="place-order-button button-primary js-place-order">
      Place your order
    </button>
  `;

   document.querySelector('.js-payment-summary')
    .innerHTML = paymentSummaryHTML;

//Step1: here when we click on place your order button it should send the post request and create a order, to create we are going to use post request and going to add all the request we are mading to save it in array and handling local storage as well to keep all the order data. first we are adding js-place-order class in place your order button so when we click that we can send req to the server.So here we are sending post request in fecth , so added object and add the method, headers and body, we have converted the carts to string since body will be string and fetch itself promise so madite it await and we can keep await only inside async fn so add async inside add event listner fn and even response.json(); is promise so added await promise means it will take time to get resposne back and need to wait until that then only next step need to go, instead of using .then we used async await which is recommended

document.querySelector('.js-place-order').addEventListener('click', async () => {

   const response  = await fetch('https://supersimplebackend.dev/orders', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      cart: carts
    })
  });

   const order = await response.json();
   

   //Step2: after we placed the order we are pushing to order array , so to orders.js file
   addToOrder(order);
   window.location.href = 'tracking.html'
});

}