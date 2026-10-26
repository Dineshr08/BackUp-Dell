
import {renderCheckoutPage} from './checkout/orderSummary.js';
import {paymentSummary} from './checkout/paymentSummary.js';
import {loadProducts, loadProductsFetch} from '../data/products.js';
import {loadCarts} from '../data/carts.js';


//step2: here we commented the first promise that we handled with fetch and returned the promise so we are using taht here. then go to test-jasmine orderSummaryTests.js to test promise

  Promise.all([
  //   new Promise ((resolve) => {
  //   loadProducts(()=> {
  //     resolve('value1');
  //   });

  // }),
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