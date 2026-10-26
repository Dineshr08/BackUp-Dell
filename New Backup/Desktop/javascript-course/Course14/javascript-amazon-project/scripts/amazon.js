// Step3 : as we commented script tag for carts.js and product.js, we need to use that here , so importing here ../ say go out of the folder. ./ say come inside the folder. So here currently we are in scripts folder and our carts.js is inside the data folder, to go there first i need to go out of scripts folder so ../ and i am in same place of data folder, come inside data then on the script location. We can call multiple export like this import {carts, addToCart} from '../data/carts.js' carts is variable and addToCart is function

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
              src="images/ratings/rating-${productItem.rating.stars * 10}.png">
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

//step5: updating the cart total qty as well in function and commenting the orginal code below

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

    //Step4: as a best practice , creating the function for each task. here adding cart action, i am creating the function.since the task is related to cart, so moving this function to carts.js, always keep the code in the relevant files
    /*
    let matchingItem;

    carts.forEach((item) => {
      if(productId === item.productId) {
        matchingItem = item;
      }
    });
  
    if (matchingItem) {
      matchingItem.quantity += 1;

    } else {
      carts.push({
        productId: productId,
        quantity: 1
      })
      
    }
      */
  //Step6: replace the code with function here
    addToCart(productId);
    updateCartQuantity();
    
    //step5: orginal code
    /*
    let totalQty = 0;

    carts.forEach((item) => {

      totalQty += item.quantity;

    });
    document.querySelector('.js-cart-quantity').innerHTML = totalQty;
    */
    

  });
});


