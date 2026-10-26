//step3: creating orders array to store the order and used local storage to store data permanently and used default operator if the so for the first time if no order placed then it will be empty
export const orders = JSON.parse(localStorage.getItem('orders')) || [];

//step4: used unshift to add the order to show in front instead of last and saved it in local storage so data will not lost when we refresh
export function addToOrder(order) {
  orders.unshift(order);
  saveToStorage();
}

function saveToStorage() {
  localStorage.setItem('orders', JSON.stringify('orders'));
}