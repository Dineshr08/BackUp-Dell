//step2: created the scripts folder and created the amazon.js file which we will be used in amazon.html file
//step4: creating the wepage. So in amazon.html html page we cannot add all the product html content, it will become very big, isntead , we are going to have the single product html content here and from that we are going to create all the product that needed for the webpage. We have all the required data in data.js file using that we are going to generate the html for the webpage
//step5: relpacing the static data to dynamic to generate the html page for the webpage. here ${productItem.rating.stars * 10} i multiply by 10 is due to the image are like save as 45, 15, 25 etc , so if we multiply 4.5 * 10 then only the name match to the image under the ratings folder. What i am doing here is ${(productItem.priceCents / 100).toFixed(2)} the output will be in 1 decimal we need 2 decimal, so .toFixed conver number to string and make it to 2 decimal. I created a template string and appended all the product html content into productHTML. this will have the complete hml content for the webpage

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
            $${(productItem.priceCents / 100).toFixed(2)}
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

//step7: Creating the html page by passing above genrated the html content to amazon.html webpage using queryselector. Now we generated the html page, next is to make it interactive
document.querySelector('.js-products-grid').innerHTML = productHTML;

//step8: when we click on add to cart need to added to the cart. So creating the carts.js file under the data and make it empty array ie carts = [];

//step9: We are making interactive, when we click on add to cart need to add the data to cart array. So we are adding js-add-to-cart-button class to above html button on Add to Cart and using querySelectorAll we are getting all the object for all the add to acrt button

addToCartElement = document.querySelectorAll('.js-add-to-cart-button');

//step10: we are iterating the all the add to cart object. Then we are adding data attribute to add to cart button . data-product-id=${products.id} here we should write it as kebab case
addToCartElement.forEach((button) => {
  button.addEventListener('click', () => {
    console.log(button.dataset);
    const productId = button.dataset.productId; //Step11: dataset will hold all the data attribute information of the button on that we are getting productID, data-product-id this kebab case will convert to like this when its inside the js object

    let matchingItem;
//step12: we arc checking if the product id is already inside the cart array , then storing that item inside the matchingItem. Cart array will have a an objects like this {productId: productId, quantity: 1}. So in below step the for the first time the cart will be empty , if the cart already has the item and the product we are trying to add is already present inside the cart array, the product id will match and that item we are storing inside the matchingItem
    carts.forEach((item) => {
      if(productId === item.productId) {
        matchingItem = item;
      }
    });
  //Step13: if the item already available inside the cart array we just increase the qty of that product, else we are adding the product to the cart
    if (matchingItem) {
      matchingItem.quantity += 1;

    } else {
      carts.push({
        productId: productId,
        quantity: 1
      })
      
    }
    //Step14: so why we do step 12 and 13 is if we click the same product again we are just increasing the qty alone, elase we add the new product to cart array

    //step16: we are adding the proper qty count from cart quantity property which has the qty for each product
    let totalQty = 0;

    carts.forEach((item) => {

      totalQty += item.quantity;

    });

    //step17: updating the final qty to the cartqty html

    document.querySelector('.js-cart-quantity').innerHTML = totalQty;
    

  });
});


