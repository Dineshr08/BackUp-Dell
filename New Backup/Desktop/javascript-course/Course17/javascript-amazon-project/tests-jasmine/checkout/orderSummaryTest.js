import {renderCheckoutPage} from '../../scripts/checkout/orderSummary.js';
import {loadFromStorage, carts} from '../../data/carts.js';

describe('test suite: renderCheckoutPage', () => {
 const productId1 = 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6'
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