import {it, describe,expect, vi, beforeEach } from 'vitest';
import userEvent from '@testing-library/user-event';
import { Products } from './Products';
import { render, screen } from '@testing-library/react';
import axios from 'axios';  

//Step8: All the axiso in the script was mocked, so no call will make to backend.
vi.mock('axios');
describe('Product Component', () => {

  let product;
  let loadCart;

  //Step3: beforeEach handled here and declared both product and loadCart above since the data ie product and loadCart is reinitating for ech test case so made that to let and initilized.
  beforeEach(() => {
    product = {
    id: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
    image: "images/products/athletic-cotton-socks-6-pairs.jpg",
    name: "Black and Gray Athletic Cotton Socks - 6 Pairs",
    rating: {
      stars: 4.5,
      count: 87
    },
    priceCents: 1090,
    keywords: ["socks", "sports", "apparel"]
  }

  loadCart = vi.fn();
  });

  

  it('Checking whether its display the proper information on the page', () => {

    
  
    render( <Products product={product} loadCart={loadCart} />);
    expect(screen.getByText('Black and Gray Athletic Cotton Socks - 6 Pairs')).toBeInTheDocument();
    expect(screen.getByText('$10.90')).toBeInTheDocument();
    expect(
      screen.getByTestId('product-image')
    ).toHaveAttribute('src', 'images/products/athletic-cotton-socks-6-pairs.jpg');

    expect(
      screen.getByTestId('product-rating-stars-image')
    ).toHaveAttribute('src', 'images/ratings/rating-45.png');

    expect(
      screen.getByText('87')
    ).toBeInTheDocument();
  });

  //Step1: Here we are doing the second step of integration setting ie user interaction.
  it('user interaction, on clicking add to cart', async () => {

  //Step2: For user interaction firest we need the page to be loaded, so added the render with product component and it has 2 props product and load cart and that is common is test case above and this, so sharing same props or data to multiple test case we can keep it hook ie beforeEach, so before each test case it will be initated and other adv of using this hook is if test case 1 modified the product data it will impact test case 2 , so by keep it in beforeEach for every test case it will keep it new data.
  render( <Products product={product} loadCart={loadCart} />);

  //Step4: To do user action we need to use userEvent that also we imported check import

  const user = userEvent.setup();
  //Step5: To get the element which needs to interacted we have added data attribute to the element ie <button className="add-to-cart-button button-primary" onClick={updateCart} data-testid="add-to-cart-button">, so using this data attribute we are get that element using screen then that we added to a variable.
    const addToCartButton = screen.getByTestId('add-to-cart-button');
    //Step6: then using userEvent we are clicking it , so so once we clicked it will take time so it will become promise so added await and added this complete it fn as asynce, only await work inside the async.
    await user.click(addToCartButton);

    //Step7: So here we are not sending request to backend , beacuse dyring testing we should not do taht, so we did mock here., so all the axios here in this script we moked that was handled above, check next step

    //Step9: Here what we are doing is just checking the call is happening properly to backend or not, below what will do is the axios post call is happening and sending with proper data or not that is what we are checking ie we are seeing whether the post call is called with proper endpoint and body data.
    expect(axios.post).toHaveBeenCalledWith(
      '/api/cart-items',
      {
        productId: 'e43638ce-6aa0-4b85-b27f-e1d07eb678c6',
        quantity: 1
      }
    );
    //Step10: Here we are checking the laod cart function is called or not
    expect(loadCart).toHaveBeenCalled();

    //Step11: Below is the actual code we tested above. which is the main code for add the data to cart

    /*
     const updateCart = async () => {

    await axios.post('/api/cart-items', {
      "productId": product.id,
      "quantity": quantity
    });

    loadCart();

  }
    */


  });
});