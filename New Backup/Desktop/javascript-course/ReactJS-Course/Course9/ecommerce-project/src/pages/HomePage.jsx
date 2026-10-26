
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

  


  return (
    <>

      <title>Ecommerce Project</title>

      <Header cart={cart} />

      <div className="home-page">
        <div className="products-grid">

          {products.map((product) => {

            

            

            return (

              <Products product={product} loadCart={loadCart} />

              

            );
          })}


        </div>
      </div>

    </>

  );
}