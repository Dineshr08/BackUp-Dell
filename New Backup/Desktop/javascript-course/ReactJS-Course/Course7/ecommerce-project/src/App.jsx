import axios from 'axios';
import { useState, useEffect } from 'react';
import { HomePage } from './pages/HomePage';
import { CheckoutPage } from './pages/CheckoutPage';
import { OrdersPage } from './pages/OrdersPage';
import { TrackingPage } from './pages/TrackingPage';
import { Routes, Route } from 'react-router';

import './App.css'

function App() {



  //Step4:Here again useEffect, same concept of Step1 only as need to run once. And passed cart as prop for Homepage and CheckoutPage below. And called cart in HomePage and CheckoutPage component function, so we can use in that component

  const [cart, setCart] = useState([]);

  useEffect(() => {
    axios.get('/api/cart-items?expand=product').then((response) => {
      setCart(response.data);
    });
  }, [])

  return (
    <>

      <Routes>
        <Route path="/" element={<HomePage cart={cart} />} />
        <Route path="checkout" element={<CheckoutPage cart={cart} />} />
        <Route path="orders" element={<OrdersPage cart={cart} />} />
        <Route path="tracking" element={<TrackingPage />} />
      </Routes>
    </>
  )
}

export default App
