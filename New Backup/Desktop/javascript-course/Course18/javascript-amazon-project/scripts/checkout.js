
import {renderCheckoutPage} from './checkout/orderSummary.js';
import {paymentSummary} from './checkout/paymentSummary.js';
import {loadProducts} from '../data/products.js';

//Step7: even this need products data so loading here just added loadProducts() here and even the same scenario here need to apply callback here as well becuase , because after that api ran need to run below 2 function, instead of creating the function and pass hereinside the loadProducts we create ananymous fn ie fn without name and apssing the 2 function, so what hap here is after we get response from the server for the api below 2 fn will run. go to tests-jasmine for test whether updated code is working fine or not and go to orderSummaryTests.js

  loadProducts(() => {
    renderCheckoutPage();
    paymentSummary();
  });
  