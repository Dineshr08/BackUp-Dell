import { HomePage } from './pages/HomePage';
import { CheckoutPage } from './pages/CheckoutPage';
import { OrdersPage } from './pages/OrdersPage';
import { TrackingPage } from './pages/TrackingPage';
import { Routes, Route} from 'react-router';

import './App.css'

function App() {
  
  //Step3: Removed the existing code and load the HomePage component here

  //Step6: Add Routes first which is were we will include all the available pages of the webiste.Each pages deetails need to mention inside the Routes. It will take 2 props one is path and element. On element we need to add the component insise {} and on path we need to give path ie after end point the webpage url eg .com/checkout. if we dont have anything after .com like homepage we can mention either "/ or index both are same and we have handled selfclosing as well here". Add imports as well for the component

  return (
    <>
    
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="checkout" element={<CheckoutPage />} />
      <Route path="orders" element={<OrdersPage />} />
      <Route path="tracking" element={<TrackingPage />} />
    </Routes>
    </>
  )
}

export default App
