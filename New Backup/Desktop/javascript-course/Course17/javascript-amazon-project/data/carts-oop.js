
function Carts(localStorageKey) {
  const carts = {
  cartsItems: undefined,
  loadFromStorage() {
  this.cartsItems = JSON.parse(localStorage.getItem(localStorageKey)); //replaced this with parameter so every object will have its own localstorage
  if(!this.cartsItems) {
    this.cartsItems = [{
      productId: 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6',
      quantity: 2,
      deliveryOptionId:'1'
    }, {
      productId: '15b6fc6f-327a-4ec4-896f-486349e85a3d',
      quantity: 1,
      deliveryOptionId:'2'
    }];
  }
  
},

saveToStorage() {
    localStorage.setItem(localStorageKey, JSON.stringify(carts));//replaced this with parameter so every object will have its own localstorage

  },

addToCart (productId) {

  let matchingItem;

    this.cartsItems.forEach((item) => {
      if(productId === item.productId) {
        matchingItem = item;
      }
    });
  
    if (matchingItem) {
      matchingItem.quantity += 1;

    } else {
      this.cartsItems.push({
        productId: productId,
        quantity: 1,
        deliveryOptionId: 1
      })
      
    }
    this.saveToStorage();
  
},
removeItemFromCart(productId) {
 

  let newCart = [];
  this.cartsItems.forEach((cartItems) => {
    if (productId !== cartItems.productId) {
      newCart.push(cartItems);

    }
  });
  this.cartsItems = newCart;
  
  this.saveToStorage();
  

},

updateDeliveryOption(productId, deliveryOptionId) {
    let matchingItem;

    this.cartsItems.forEach((cartItem) => {
      if (productId === cartItem.productId) {
        matchingItem = cartItem;
      }
    });

    matchingItem.deliveryOptionId = deliveryOptionId;

    this.saveToStorage();
}

}

return carts;

}




const carts = Carts('carts-oop');
const businessCarts = Carts('businessCarts');

carts.loadFromStorage();
businessCarts.loadFromStorage();





 

  



  
