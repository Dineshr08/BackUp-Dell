
import axios from 'axios';
import dayjs from 'dayjs';
import { useState, useEffect } from 'react';
import { Link } from 'react-router';
import { formatMoney } from '../utils/money'
import './checkout-header.css';
import './CheckoutPage.css';

export function CheckoutPage({ cart }) {

  const [deliveryOptions, setDeliveryOptions] = useState([]);
  const [paymentSummary, setPaymentSummary] = useState('');

  useEffect(() => {

    axios.get('/api/delivery-options?expand=estimatedDeliveryTime')
      .then((response) => {
        console.log(response.data);
        setDeliveryOptions(response.data);
      })

      //Step7: Here got the data from payment summary api and used async await instead of then to handle async code and here  const [paymentSummary, setPaymentSummary] = useState(null); used null as initila value as the input of payment summary will be object instead of array

      // axios.get('/api/payment-summary')
      // .then((response) => {
      //   setPaymentSummary(response.data);
      // });

      const payment = async() => {
        const response = await axios.get('/api/payment-summary');
        console.log(response.data);
        setPaymentSummary(response.data);

      }
      payment();

  }, []);

  //Step5: Here based on the data in cart we are creating the checkout page cart item with one html and following all how we did for creating multiple products, eg passing keys, subsituting name etc using map. Here we are doing one additional steps as subsitution value for this $10.90 we are doing some manual operation in both homepage and checkout page so we are creating function for this . So Creating utils folder under src and creating mondy.js file and writing function there and calling same here
  return (

    <>
      <title>Checkout</title>
      <div className="checkout-header">
        <div className="header-content">
          <div className="checkout-header-left-section">
            <Link to="/">
              <img className="logo" src="images/logo.png" />
              <img className="mobile-logo" src="images/mobile-logo.png" />
            </Link >
          </div>

          <div className="checkout-header-middle-section">
            Checkout (<Link className="return-to-home-link"
              to="/">3 items</Link >)
          </div>

          <div className="checkout-header-right-section">
            <img src="images/icons/checkout-lock-icon.png" />
          </div>
        </div>
      </div>

      <div className="checkout-page">
        <div className="page-title">Review your order</div>

        <div className="checkout-grid">
          <div className="order-summary">

            {deliveryOptions.length > 0 && cart.map((cartItem) => {

              
              const selectDeliveryOption = deliveryOptions.find((deliveryOption) => {
                return deliveryOption.id === cartItem.deliveryOptionId
              })

              return (
                <div key={cartItem.productId} className="cart-item-container">
                  <div className="delivery-date">
                    
                    Delivery date: {dayjs(selectDeliveryOption.estimatedDeliveryTimeMs).format('dddd, MMMM D')}
                  </div>

                  <div className="cart-item-details-grid">
                    <img className="product-image"
                      src={cartItem.product.image} />

                    <div className="cart-item-details">
                      <div className="product-name">
                        {cartItem.product.name}
                      </div>
                      <div className="product-price">
                        {formatMoney(cartItem.product.priceCents)}
                      </div>
                      <div className="product-quantity">
                        <span>
                          Quantity: <span className="quantity-label">{cartItem.quantity}</span>
                        </span>
                        <span className="update-quantity-link link-primary">
                          Update
                        </span>
                        <span className="delete-quantity-link link-primary">
                          Delete
                        </span>
                      </div>
                    </div>

                    <div className="delivery-options">
                      <div className="delivery-options-title">
                        Choose a delivery option:
                      </div>

                    {/*Step6: Again same like Step5 with one delivery option we have created 3 delivery option using map and used key and dayjs libaray to create a date and used delivery-options api to get the delivey option data and its estimated time etc  . Here we used name={`delivery-option-${cartItem.productId}`} /> product id, becaise if we have 3 radio option if all the radio option has same name then only we can able to select one and checked={deliveryOption.id === cartItem.deliveryOptionId} based on the deliveryoption id in cart we have checked that radio button by default and based on delivery option in cart we have created the data as well.*/}


                      {deliveryOptions.map((deliveryOption) => {

                        let priceString = 'FREE Shipping';

                        if (deliveryOption.priceCents > 0) {
                          priceString = `${formatMoney(deliveryOption.priceCents)} - Shipping`;
                        }

                        return (
                          <div key={deliveryOption.id} lassName="delivery-option">
                            <input type="radio"
                              checked={deliveryOption.id === cartItem.deliveryOptionId}
                              className="delivery-option-input"
                              name={`delivery-option-${cartItem.productId}`} />
                            <div>
                              <div className="delivery-option-date">
                                {dayjs(deliveryOption.estimatedDeliveryTimeMs).format('dddd, MMMM D')}
                              </div>
                              <div className="delivery-option-price">
                                {priceString}
                              </div>
                            </div>
                          </div>
                        );
                      })}

                    </div>
                  </div>
                </div>
              );

            })}

          </div>

{/*Step8:Here used payment summary api and update the data directly */}
          <div className="payment-summary">
            <div className="payment-summary-title">
              Payment Summary
            </div>

            <div className="payment-summary-row">
              <div>Items ({paymentSummary.totalItems}):</div>
              <div className="payment-summary-money">{formatMoney(paymentSummary.productCostCents)}</div>
            </div>

            <div className="payment-summary-row">
              <div>Shipping &amp; handling:</div>
              <div className="payment-summary-money">{paymentSummary.shippingCostCents}</div>
            </div>

            <div className="payment-summary-row subtotal-row">
              <div>Total before tax:</div>
              <div className="payment-summary-money">{paymentSummary.totalCostBeforeTaxCents}</div>
            </div>

            <div className="payment-summary-row">
              <div>Estimated tax (10%):</div>
              <div className="payment-summary-money">{paymentSummary.taxCents}</div>
            </div>

            <div className="payment-summary-row total-row">
              <div>Order total:</div>
              <div className="payment-summary-money">{paymentSummary.totalCostCents}</div>
            </div>

            <button className="place-order-button button-primary">
              Place your order
            </button>
          </div>
        </div>
      </div>
    </>


  );
}