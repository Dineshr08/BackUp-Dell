

import {carts, addToCart} from '../data/carts.js';
import {products, loadProducts} from '../data/products.js';
import {formatCurrency} from './utils/money.js';
let productHTML = '';

//Step4: here we uuse products to generate the html but now the product data lies inside the function loadProducts(), so calling that here so we can access the class objects inside that. but problem here after we called the loadProducts() fn still we see the empty page in ui, the reason is the fn loadProducts() takes time and it asyncfunction it wont wait until its gets back the response so as soon as the loadProducts execute the below loop started executed and by the time loop execute the loadProducts fn did not get response so the below loop has empty data so nothing loads in the page. so to fix this after we get response of the loadProducts fn we need to run below code , so creating below code as function and moving that fn inside the loadProducts addEventlistner and exporting renderProductPage fn so can use in otheer places. function is value so can pass fn inside the function. so commenting loadProducts(); and passing the fn for our example. go back to product .js

// loadProducts();

loadProducts(renderProductPage);

export function renderProductPage() {
  products.forEach((productItem) => {
    productHTML += `
      <div class="product-container">
            <div class="product-image-container">
              <img class="product-image"
                src="${productItem.image}">
            </div>

            <div class="product-name limit-text-to-2-lines">
              ${productItem.name}
            </div>

            <div class="product-rating-container">
              <img class="product-rating-stars"
                src="${productItem.getRating()}">
              <div class="product-rating-count link-primary">
                ${productItem.rating.count}
              </div>
            </div>

            <div class="product-price">
              $${formatCurrency(productItem.priceCents)}
            </div>

            <div class="product-quantity-container">
              <select>
                <option selected value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
              </select>
            </div>

            <div class="product-spacer"></div>

            ${productItem.getSizeHTML()}

            <div class="added-to-cart">
              <img src="images/icons/checkmark.png">
              Added
            </div>

            <button class="add-to-cart-button button-primary js-add-to-cart-button" data-product-id=${productItem.id}>
              Add to Cart
            </button>
          </div>        
    `

  });


  document.querySelector('.js-products-grid').innerHTML = productHTML;



  function updateCartQuantity() {
        let totalQty = 0;

        carts.forEach((item) => {

        totalQty += item.quantity;

      });
      
      document.querySelector('.js-cart-quantity').innerHTML = totalQty;

      }

  const addToCartElement = document.querySelectorAll('.js-add-to-cart-button');
  addToCartElement.forEach((button) => {
    button.addEventListener('click', () => {
      console.log(button.dataset);
      const productId = button.dataset.productId; 

      
      addToCart(productId);
      updateCartQuantity();
      
      
    });
  });

}
