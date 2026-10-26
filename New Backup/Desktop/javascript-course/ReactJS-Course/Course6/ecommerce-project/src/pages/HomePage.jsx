
//Step2: Moved homepage html content into the component, then replaceing all class= to className=.Then moving all the css related to the this home page as well inside the pages folder.And import that here too.
/* Below 3 are homepage related css. Complete index.css is related to website related css so moving that to react index.css. Then moving header.css and gendral.css inside the pages and renaming the genrall.css to HomePage.css. Impoting both here
<Link  rel="stylesheet" to="styles/shared/general.css">
    <Link  rel="stylesheet" to="styles/shared/header.css">
    <Link  rel="stylesheet" to="styles/pages/index.css">
    */
//All the image is currently available inside the images folder that we move directly to public, we usually keep images inside the assets folder but here we move into public, becuase in below html code all image location was kept like this src="images/mobile-logo-white.png" />so it will directly refer to public image folder, but if we move to assets it willtake lot of rework. So as now for practise we move to public folder.

//Remove all the data inside App.css

import './HomePage.css'
import {Header} from '../components/Header'
import { Link } from 'react-router';
export function HomePage() {

  //Step11: Then removing the existing code in homepage.jsx and orders.jsx and added the <Header \> component
  return (

    <>

      <title>Ecommerce Project</title>
    
    <Header />  

    <div className="home-page">
      <div className="products-grid">
        <div className="product-container">
          <div className="product-image-container">
            <img className="product-image"
              src="images/products/athletic-cotton-socks-6-pairs.jpg" />
          </div>

          <div className="product-name limit-text-to-2-lines">
            Black and Gray Athletic Cotton Socks - 6 Pairs
          </div>

          <div className="product-rating-container">
            <img className="product-rating-stars"
              src="images/ratings/rating-45.png" />
            <div className="product-rating-count link-primary">
              87
            </div>
          </div>

          <div className="product-price">
            $10.90
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

        <div className="product-container">
          <div className="product-image-container">
            <img className="product-image"
              src="images/products/intermediate-composite-basketball.jpg" />
          </div>

          <div className="product-name limit-text-to-2-lines">
            Intermediate Size Basketball
          </div>

          <div className="product-rating-container">
            <img className="product-rating-stars"
              src="images/ratings/rating-40.png" />
            <div className="product-rating-count link-primary">
              127
            </div>
          </div>

          <div className="product-price">
            $20.95
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

        <div className="product-container">
          <div className="product-image-container">
            <img className="product-image"
              src="images/products/adults-plain-cotton-tshirt-2-pack-teal.jpg" />
          </div>

          <div className="product-name limit-text-to-2-lines">
            Adults Plain Cotton T-Shirt - 2 Pack
          </div>

          <div className="product-rating-container">
            <img className="product-rating-stars"
              src="images/ratings/rating-45.png" />
            <div className="product-rating-count link-primary">
              56
            </div>
          </div>

          <div className="product-price">
            $7.99
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
      </div>
    </div>

    </>

  );
}