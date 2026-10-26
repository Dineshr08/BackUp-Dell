import axios from 'axios';
import { useState, useEffect } from 'react';
import { HomePage } from './pages/HomePage';
import { CheckoutPage } from './pages/CheckoutPage';
import { OrdersPage } from './pages/OrdersPage';
import { TrackingPage } from './pages/TrackingPage';
import { Routes, Route } from 'react-router';

import './App.css'

function App() {





  const [cart, setCart] = useState([]);

  const loadCart = async () => {
    await axios.get('/api/cart-items?expand=product').then((response) => {
      setCart(response.data);
    });
  }

  //Step3: commented below earlier we have kept get call inside the useeffect, but now we have created as fn and called inside, the reason, is to auto refresh the cart once the we perfrom add to cart, elase we need to refersh manually

  useEffect(() => {
    // axios.get('/api/cart-items?expand=product').then((response) => {
    //   setCart(response.data);
    // });

    loadCart();
  }, [])

  return (
    <>

      <Routes>
        <Route path="/" element={<HomePage cart={cart} loadCart={loadCart}/>} />
        <Route path="checkout" element={<CheckoutPage cart={cart} loadCart={loadCart} />} />
        <Route path="orders" element={<OrdersPage cart={cart} />} />
        <Route path="tracking" element={<TrackingPage />} />
      </Routes>
    </>
  )
}

export default App
