
//step1: intially it was like this we have modified this code to function and called


// export let carts = carts = JSON.parse(localStorage.getItem('carts'));
//   if(!carts) {
//     carts = [{
//       productId: 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6',
//       quantity: 2,
//       deliveryOptionId:'1'
//     }, {
//       productId: '15b6fc6f-327a-4ec4-896f-486349e85a3d',
//       quantity: 1,
//       deliveryOptionId:'2'
//     }];
//   }

export let carts;

export function loadFromStorage() {

  carts = JSON.parse(localStorage.getItem('carts'));
  if(!carts) {
    carts = [{
      productId: 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6',
      quantity: 2,
      deliveryOptionId:'1'
    }, {
      productId: '15b6fc6f-327a-4ec4-896f-486349e85a3d',
      quantity: 1,
      deliveryOptionId:'2'
    }];
  }
  
}

//step2: called this function here
loadFromStorage();

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
        quantity: 1,
        deliveryOptionId: 1
      })
      
    }

    
    saveToStorage();
  
}

export function removeItemFromCart(productId) {
 

  let newCart = [];
  carts.forEach((cartItems) => {
    if (productId !== cartItems.productId) {
      newCart.push(cartItems);

    }
  });
  carts = newCart;
  
  saveToStorage();
  

}

 

  function saveToStorage() {
    localStorage.setItem('carts', JSON.stringify(carts));

  }

  //step8: now based on the data we have in cart we are showing up the data, but now we are making it interactive, so if we choose the different delivery option we need to update the delivery date and update in cart as well to do that we need to know the product that we are change the delivery option and whoch delivery option we are going to change , so that 2 we give as parameter, then to get the product that we are going to update we have written the code below. so from carts we get getting the matching product and updating the delivery options based on the paramenter, as this is related to cart so we have written in carts.js file as function

  export function updateDeliveryOption(productId, deliveryOptionId) {
    let matchingItem;

    carts.forEach((cartItem) => {
      if (productId === cartItem.productId) {
        matchingItem = cartItem;
      }
    });
    // console.log(matchingItem);

    matchingItem.deliveryOptionId = deliveryOptionId;

    saveToStorage();
}
