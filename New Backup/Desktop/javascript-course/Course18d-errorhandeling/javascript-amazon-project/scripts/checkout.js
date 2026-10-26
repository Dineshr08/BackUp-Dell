
import {renderCheckoutPage} from './checkout/orderSummary.js';
import {paymentSummary} from './checkout/paymentSummary.js';
import {loadProducts, loadProductsFetch} from '../data/products.js';
import {loadCarts} from '../data/carts.js';





  //Error handeling : Step3 - Added error handeling for async await so commenting below

  /*
  async function loadPage() {
  await loadProductsFetch();

   const value = await new Promise((resolve) => {
      loadCarts(() => {
        resolve('value1');
      });
    });

    renderCheckoutPage();
    paymentSummary();
} 
    */

async function loadPage() {
  await loadProductsFetch();

  try {
    const value = await new Promise((resolve) => {
      loadCarts(() => {
        resolve('value1');
      });
    });
  } catch(error) {
    console.log('Unexpected error please try again');
  }
    renderCheckoutPage();
    paymentSummary();
} 


loadPage();