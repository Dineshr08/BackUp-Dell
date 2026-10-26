
import {renderCheckoutPage} from './checkout/orderSummary.js';
import {paymentSummary} from './checkout/paymentSummary.js';
import {loadProducts} from '../data/products.js';
import {loadCarts} from '../data/carts.js';


//Step1: below are the same thing we are going to do with promise  and below was gng to comment as its used callback
  // loadProducts(() => {
  //   renderCheckoutPage();
  //   paymentSummary();
  // });

//Step2: in carts.js created loadCarts function as well to run multiple promises to run in parallael or to see the example after load the product it has to wait then load the carts it has to wait then run the next code check this behaivior we have crated that fn

//step3: creating the promise first it load the all products then load all the carts then run the next step ie then
/*
  new Promise ((resolve) => {
    loadProducts(()=> {
      resolve('value1');
    });

  }).then((value) => {
    return new Promise((resolve) => {
      console.log(value);

      loadCarts(() => {
        resolve();
      });

    }).then(() => {
      renderCheckoutPage();
      paymentSummary();
    });
  });
  */
  //Step4: running all promise in parallel so commenting above. move all promise inside the array

  Promise.all([
    new Promise ((resolve) => {
    loadProducts(()=> {
      resolve('value1');
    });

  }),
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