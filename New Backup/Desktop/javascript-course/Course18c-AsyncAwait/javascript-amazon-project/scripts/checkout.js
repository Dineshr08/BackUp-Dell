
import {renderCheckoutPage} from './checkout/orderSummary.js';
import {paymentSummary} from './checkout/paymentSummary.js';
import {loadProducts, loadProductsFetch} from '../data/products.js';
import {loadCarts} from '../data/carts.js';



//Step1: commenting below as we gng to use async await
/*
  Promise.all([
 
  loadProductsFetch(),
  new Promise((resolve) => {
      

      loadCarts(() => {
        resolve();
      });

    })
  ]).then((value) => {
    console.log(value);
    renderCheckoutPage();
    paymentSummary();
  });
  */

  //Error handeling : Step3 - Added error handeling for async

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

//Step2: to run this fn just call like normal fn
loadPage();