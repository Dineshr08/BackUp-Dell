import {carts} from '../../data/carts.js';
import {products} from '../../data/products.js';
import {deliveryOptions} from '../../data/deliveryOption.js';
import {formatCurrency} from '../utils/money.js';

//step14: here we are calculating the cost based on the data available in the cart, and writing the code in function so we can call that in checkout.js file because that is main file which called in checkout.html


export function paymentSummary() {

  //step16: to find the total cost of the produt in cart and total tax we are doing below, first we are getting the matching product then totalling that with qty then based on the delivery option in cart and comparing with deliveryoptioin array then getting total delivery option cost
  
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

  //step17: store all the data to variables 
  const totalBeforeTaxCents = productPriceCents + shippingPriceCents;
  const taxCents = totalBeforeTaxCents * 0.1;
  const totalCents = totalBeforeTaxCents + taxCents;

  //step18: replace to the html

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

    <button class="place-order-button button-primary">
      Place your order
    </button>
  `;

   document.querySelector('.js-payment-summary')
    .innerHTML = paymentSummaryHTML;


}