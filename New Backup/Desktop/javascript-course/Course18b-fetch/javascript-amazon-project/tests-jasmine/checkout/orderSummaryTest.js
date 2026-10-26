import {renderCheckoutPage} from '../../scripts/checkout/orderSummary.js';
import {loadFromStorage, carts} from '../../data/carts.js';
import {loadProducts} from '../data/products.js';

describe('test suite: renderCheckoutPage', () => {
 const productId1 = 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6'

 //step3: commenting below as we are going to use that function loadProductsFetch() here and test, we replaced that as loadProductsFetch return promise so used .then and it will take fn and inside it we passed done() so it will go to next steps


    beforeAll((done) => {

      loadProductsFetch().then( () =>{
        done();
      })
    // loadProducts(() => {
    //   done();
    // });
  });

  beforeEach(() => {
    spyOn(localStorage, 'setItem');
    
    spyOn(localStorage, 'getItem').and.callFake(() => {
        return JSON.stringify([{
          productId: productId1,
          quantity: 1,
          deliveryOptionId: '1'
        }]);
      });
    loadFromStorage();

    document.querySelector('.js-test-container').innerHTML = `<div class="js-order-summary"></div>`

    renderCheckoutPage();
  });

  afterEach(() => {
    document.querySelector('.js-test-container').innerHTML = '';
  });
  

  it('How the page looks', () => {

    expect(document.querySelectorAll('.js-cart-item-container').length).toEqual(1);
    expect(document.querySelector(`.js-product-quantity-${productId1}`).innerText).toContain('Quantity: 1');

  });

  it('How the page behaves when we click delete button', () => {
    

    document.querySelector(`.js-delete-quantity-${productId1}`).click();
    expect(document.querySelectorAll(`.js-delete-quantity`).length).toEqual(0);
    expect(carts.length).toEqual(0);
    



  });
});