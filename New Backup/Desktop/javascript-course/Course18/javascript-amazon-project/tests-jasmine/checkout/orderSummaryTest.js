import {renderCheckoutPage} from '../../scripts/checkout/orderSummary.js';
import {loadFromStorage, carts} from '../../data/carts.js';
import {loadProducts} from '../data/products.js';

describe('test suite: renderCheckoutPage', () => {
 const productId1 = 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6'

 //step8: here renderCheckoutPage(); need producst data so loading that fn here and i dont want to load that in all the test case everytime i need to load that once so i am using beforeAll() hook. and here also facing the same problem because test case till fail because the loadProductstake time to get back response and before getting response , below code run so still test case failed to over come that all  all beforeall(), beforeeach(), it(), have parameter called done, if we pass that and until we call that done(); function explictly it wont go to next lines .so commeting below code 

  // beforeAll(() => {
  //   loadProducts();
  // });

  //Step9:so what we done here is we passed that parameter and for loadProducts fn we passed this function, so after we get response from loadProducts we pass done();function, so once done is executed then it will move to next line of codes so our problem resolved  so it will wait until we get response from the  server. done is inbuilt fn of jasmine framework

    beforeAll((done) => {
    loadProducts(() => {
      done();
    });
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