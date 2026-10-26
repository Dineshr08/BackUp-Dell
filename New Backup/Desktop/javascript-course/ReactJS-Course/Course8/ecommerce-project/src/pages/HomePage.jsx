
import axios from 'axios';
import { useState, useEffect } from 'react';
import './HomePage.css'
import { Header } from '../components/Header'
import { Link } from 'react-router';
import {Products} from './Products'




export function HomePage({ cart, loadCart }) {

  const [products, setProducts] = useState([]);
  // const [cart, setCart] = useState([]);

  useEffect(() => {
    axios.get('/api/products').then((response) => {
      setProducts(response.data);
    });

  }, []);

  //Step4: Here we are dynamically handeling the add to cart quantity, so stored the data in state and used onchage and value to get the current qty we selected.


  // const [quantity, setQuantity] = useState(1);

  // const updateQuantity = (event) => {
  //   const selectedQuantity = Number(event.target.value);
  //   setQuantity(selectedQuantity);

  // }


  return (
    <>

      <title>Ecommerce Project</title>

      <Header cart={cart} />

      <div className="home-page">
        <div className="products-grid">

          {products.map((product) => {

            //Step2: Here is the fn, it will update the cart, we have used post call and data for post and put should be add inside {} like object and we have called loadCart fn here , this is due to once the cart is updated the loadcart fn will run so the page will update automatically instead of referesh

            // const updateCart = async () => {

            //   await axios.post('/api/cart-items', {
            //     "productId": product.id,
            //     "quantity": quantity
            //   });

            //   loadCart();

            // }

            

            return (

              <Products product={product} loadCart={loadCart} />

              //Step6: We have commented below and created seperate jsx for products as if i use state at top const [quantity, setQuantity] = useState(1); it will apply for all the products , eg if i choose qty for one product the same qty is reflecting for all the product, so inorder to fox this we have created the seperated component and also cant use state below here, the resaone the all hook should be placed in top of the compoenet so created seperate component and handled.

              // <div key={product.id} className="product-container">
              //   <div className="product-image-container">
              //     <img className="product-image"
              //       src={product.image} />
              //   </div>

              //   <div className="product-name limit-text-to-2-lines">
              //     {product.name}
              //   </div>

              //   <div className="product-rating-container">
              //     <img className="product-rating-stars"
              //       src={`images/ratings/rating-${product.rating.stars * 10}.png`} />
              //     <div className="product-rating-count link-primary">
              //       {product.rating.count}
              //     </div>
              //   </div>

              //   <div className="product-price">
              //     ${(product.priceCents / 100).toFixed(2)}
              //   </div>

              //   <div className="product-quantity-container" >

              //Step5:here we have handled on how to get the value for the qty, we used value property which will tell what value we selected and the onchange will run the fn, the fn has event paramater and from that we can get the value we selected etc.

              //     <select value={quantity} onChange={updateQuantity}>
              //       <option value="1">1</option>
              //       <option value="2">2</option>
              //       <option value="3">3</option>
              //       <option value="4">4</option>
              //       <option value="5">5</option>
              //       <option value="6">6</option>
              //       <option value="7">7</option>
              //       <option value="8">8</option>
              //       <option value="9">9</option>
              //       <option value="10">10</option>
              //     </select>
              //   </div>

              //   <div className="product-spacer"></div>

              //   <div className="added-to-cart">
              //     <img src="images/icons/checkmark.png" />
              //     Added
              //   </div>

              //Step1: We are using onClick event handler, it will run the function when we are clicking the button.Fn written above

              //   <button className="add-to-cart-button button-primary" onClick={updateCart}>
              //     Add to Cart
              //   </button>
              // </div>

            );
          })}


        </div>
      </div>

    </>

  );
}