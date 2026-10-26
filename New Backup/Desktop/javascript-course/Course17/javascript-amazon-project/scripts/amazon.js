

import {carts, addToCart} from '../data/carts.js';
import {products} from '../data/products.js';
import {formatCurrency} from './utils/money.js';
let productHTML = '';

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


