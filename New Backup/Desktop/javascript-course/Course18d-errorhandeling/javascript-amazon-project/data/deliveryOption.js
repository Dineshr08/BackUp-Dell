// Step1: created deliveryOption.js, which store the each product in cart deliver option details like delivery time, deliver proice etc. We can add this details on product list itself, but we are going to create a seperate array and storing that details the reason is the duplication of data, for example, if we have 10 product 7 product may have same delivery option like free shiping so rewriying the same lines on each product will be difficult, instead we are creating the deliverOption arruy and will give id for each deliver option in our case we have 3 , so those id we will pass to product, this approch is normalize the data will no need to duplicate the data in product array

export const deliveryOptions = [{
  id:'1',
  deliveryDays: 7,
  priceCents:0
}, {
  id:'2',
  deliveryDays: 3,
  priceCents:499
}, {
  id:'3',
  deliveryDays: 1,
  priceCents:999
}];