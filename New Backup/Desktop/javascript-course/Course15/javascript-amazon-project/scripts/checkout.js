
import {renderCheckoutPage} from './checkout/orderSummary.js';
import {paymentSummary} from './checkout/paymentSummary.js';

  //step10: the above whole code we are moving iside the function so for examople after each update the complete code has to rerun ie render inorder to do that we are creating the function after performing some updates we will reload the page by calling the function, in our code after delete or updatedeliber option we will rerender the page

  renderCheckoutPage();

  //Step13: in UI we have order summary and paymenet summary data, so we are going to create two seperate file for bott orderSummary.js and paymentSummary.js under the checkout folder which will be created under scripts. All above code is related to order summary apart from   renderCheckoutPage(); this so moving everuthing there. After moving need to update the import location as well and adding export for  renderCheckoutPage(); function  

  //step15:calling   paymentSummary(); fn here 

  paymentSummary();