
import axios from 'axios';
import { useState, useEffect } from 'react';
import './HomePage.css'
import { Header } from '../components/Header'
import { Link } from 'react-router';


//Step1: We have get the products data from api and made the homepage cart , we have used axios to send the request and used axios inside the useeffect, the reason is if i navigate to home page everytime i come i will send request to products api instead od that for the first time alone i need to send api and get the data so used useeffect and given [] on use effect, so it will run once when the component is created. then passed the products data in updater function ie setProducts so , it will update the products array, so we have used the state. and declared with initial value as [] array, same concept applied for cart as well, then the same passed in header with props <Header cart={cart}/> as header is seperate component. Once we have the products data with one product html we have created html for all products by calling them below with looping through map {products.map((product) => { return (, it will create an array of elements, since we are having array of elements si in react we need to add key so we added key and passed product.id which is unique for each product. Handled below as well
/*
On vite.config.js if we add this under plugin, on giving end point to axiso.get no need to mention the full end point mainly baseurl, insitead of base url we can start giving with /api/path of the api since the base url was configured here
server: {
  proxy: {
    '/api': {
      target:'http://localhost:3000'
    },
    '/image': {
      target: 'http://localhost:3000'
    }
  }
} And below too
 To add / inforont of all relative urls
<base href="/" />
Eg: Relative url
images/products/shirt.png this will convert to below if we add <base href="/" /> in index.html below <meta element
/images/products/shirt.png
  */

export function HomePage( {cart} ) {

  const [products, setProducts] = useState([]);
  // const [cart, setCart] = useState([]);

  useEffect(() => {
    axios.get('/api/products').then((response) => {
      setProducts(response.data);
    });
    //Step3: As now we are going to display data in checkout page based on the data available in below api, but we cant run the same api again when we go to checkout page, so what we are doing is lifting up the state to app component and pass the cart via props to homepage and checkout page. So comment below and above usestate too of cart
    // axios.get('/api/cart-items').then((response) => {
    //   setCart(response.data);
    // });
  }, []);


  return (
    <>

      <title>Ecommerce Project</title>

      <Header cart={cart}/>

      <div className="home-page">
        <div className="products-grid">

          {products.map((product) => {
            return (
              <div key={product.id} className="product-container">
                <div className="product-image-container">
                  <img className="product-image"
                    src={product.image} />
                </div>

                <div className="product-name limit-text-to-2-lines">
                  {product.name}
                </div>

                <div className="product-rating-container">
                  <img className="product-rating-stars"
                    src={`images/ratings/rating-${product.rating.stars * 10}.png`} />
                  <div className="product-rating-count link-primary">
                    {product.rating.count}
                  </div>
                </div>

                <div className="product-price">
                  ${(product.priceCents / 100).toFixed(2)}
                </div>

                <div className="product-quantity-container">
                  <select>
                    <option value="1">1</option>
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

                <div className="product-spacer"></div>

                <div className="added-to-cart">
                  <img src="images/icons/checkmark.png" />
                  Added
                </div>

                <button className="add-to-cart-button button-primary">
                  Add to Cart
                </button>
              </div>

            );
          })}


        </div>
      </div>

    </>

  );
}