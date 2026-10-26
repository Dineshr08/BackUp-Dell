
//Step10: If we have a common thing eg header tab is common in both homepage and order page so such thing we need to convert to a component. So the common component we need to add inside the component folder inside the src, for the things which is specific to page that need to keep in page component, so now we are moving that data from homepage and orders to header componet.Then in our all component html we use <Link and its prop to= to switch the pages, eg when we click order from home page it will take us there, but it will reload the page if we use <Link instead we will use <Link  component and its prop to= so iinstead of reloading it will take us there. <Link = <Link  and to= is equal to to=. We also move therespectibe header.css here. Then removing the existing code in homepage.jsx and orders.jsx and added the <Header \> component

import './header.css';
import { Link } from 'react-router';

export function Header() {

  return (
    <div className="header">
      <div className="left-section">
        <Link to="/" className="header-link">
          <img className="logo"
            src="images/logo-white.png" />
          <img className="mobile-logo"
            src="images/mobile-logo-white.png" />
        </Link >
      </div>

      <div className="middle-section">
        <input className="search-bar" type="text" placeholder="Search" />

        <button className="search-button">
          <img className="search-icon" src="images/icons/search-icon.png" />
        </button>
      </div>

      <div className="right-section">
        <Link className="orders-link header-link" to="/orders">

          <span className="orders-text">Orders</span>
        </Link >

        <Link className="cart-link header-link" to="/checkout">
          <img className="cart-icon" src="images/icons/cart-icon.png" />
          <div className="cart-quantity">3</div>
          <div className="cart-text">Cart</div>
        </Link >
      </div>
    </div>
  );
}