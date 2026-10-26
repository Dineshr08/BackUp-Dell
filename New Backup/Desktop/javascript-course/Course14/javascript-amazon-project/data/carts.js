//Step2 - Update the variable or function which need to be exported, which means that are going to use in other files. Updating in all the required places
// export let carts = [];

//step9: from this "export let carts = [];" to updating below. refer step8 for more details why we do this and commenting above line and refer step 27 as well

//  export let carts = [{
//     productId: 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6',
//     quantity: 2,
//   }, {
//     productId: '15b6fc6f-327a-4ec4-896f-486349e85a3d',
//     quantity: 1
//   }];

//step27: we need to get the data as well like above so doing get operation, as our first step is to need carts object from that only we can proceed so i am comenting the above line 

export let carts = JSON.parse(localStorage.getItem('carts'));

//step28: if there is no item in cart by default it will show 2 item in cart summary
if(carts.length === 0) {
  carts = [{
    productId: 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6',
    quantity: 2,
  }, {
    productId: '15b6fc6f-327a-4ec4-896f-486349e85a3d',
    quantity: 1
  }];
}

export function addToCart (productId) {

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

    //step26: after add to cart we have to keep the data permenant os calling localstorage here
    saveToStorage();
  
}

export function removeItemFromCart(productId) {
  //step21: creating the new array and compare with cartitems product id  with delete product id, if both not matched then added to new cart, then finallay reassigning that to cart, so the cart will have the item which is available only

  let newCart = [];
  carts.forEach((cartItems) => {
    if (productId !== cartItems.productId) {
      newCart.push(cartItems);

    }
  });
  carts = newCart;
  //step25: after remove we have to keep the data permenant os calling localstorage here
  saveToStorage();
  

}

  //step24: our next issue is when we reload the page the change or delete we made is disapper to fix that we are using localstorage and going to create a fn to setItem and this we are creating in carts.js

  function saveToStorage() {
    localStorage.setItem('carts', JSON.stringify(carts));

  }
