import { it, expect, describe, vi, beforeEach } from 'vitest';
import { render, screen, within } from '@testing-library/react';
import { MemoryRouter } from 'react-router';
import axios from 'axios';
import { HomePage } from './HomePage';

vi.mock('axios');

//Step1: Here we are uing mock implementation and testing the homepage component. On home page we use get api to get the data and displaying in the UI, and we cant use axios.get directly in testing script os we implemented mock implementation.
describe('HomePage component', () => {
  let loadCart;

  beforeEach(() => {
    loadCart = vi.fn();
//Step2: What we did here is whenever axios.get is called it will run this mock implementation and return the data inside it.So in orginal axiso.get we passed the endpoint url, so mock implementation will take the function and inside that we are passing urlpath, ie in  orginal 
/*
axios.get('/api/products').then((response) => {
      setProducts(response.data);
    });
we have passed '/api/products' so in mock implemenation we take that url path and if that path is same then it will return the 2 product and we have to return in same way how orginal api will return . in orginal it will return in object with property as dataand it will value inside array so same way we are returning
*/
    axios.get.mockImplementation(async (urlPath) => {
      if (urlPath === '/api/products') {
        return {
          data: [{
            id: "e43638ce-6aa0-4b85-b27f-e1d07eb678c6",
            image: "images/products/athletic-cotton-socks-6-pairs.jpg",
            name: "Black and Gray Athletic Cotton Socks - 6 Pairs",
            rating: {
              stars: 4.5,
              count: 87
            },
            priceCents: 1090,
            keywords: ["socks", "sports", "apparel"]
          },
          {
            id: "15b6fc6f-327a-4ec4-896f-486349e85a3d",
            image: "images/products/intermediate-composite-basketball.jpg",
            name: "Intermediate Size Basketball",
            rating: {
              stars: 4,
              count: 127
            },
            priceCents: 2095,
            keywords: ["sports", "basketballs"]
          }]
        };
      }
    });
  });

  it('displays the products correct', async () => {

    //Step3: So now we are rendering , but the next issue is <MemoryRouter> here earlier we have not used, why we used is in home page component we have header component and inside header we have <Link componet, if we used link it should be inisde the <BrowserRouter>, so for testing we need to use <MemoryRouter>, refer main.jsx for how we have used <BrowserRouter>.
    render(
      <MemoryRouter>
        <HomePage cart={[]} loadCart={loadCart} />
      </MemoryRouter>
    );

    //Step4: Then on each prduct we have added data atribute called product-container <div key={product.id} className="product-container"data-testid="product-container" /> and using that we are passing some unique data to all the product.this findAllByTestId will take all element which has that data attribute, why we used findAllByTestId instead of getAllByTestId, becuase get will get the data in page , but find will wait until the page loaded then get the element, our case we are generate the html firest then need to take the data so need to use find.
    const productContainers = await screen.findAllByTestId('product-container');

    //Step4: then we are validating with 2 product is diaplayed in webpage
    expect(productContainers.length).toBe(2);

    //Step5:We are validating the name is displayed in the webpage
    expect(
      within(productContainers[0])
        .getByText('Black and Gray Athletic Cotton Socks - 6 Pairs')
    ).toBeInTheDocument();

    expect(
      within(productContainers[1])
        .getByText('Intermediate Size Basketball')
    ).toBeInTheDocument();
  });

  //Step6: Overall we are invoking the homepage component , passed the fake data using data implementation and checking the page is loaded or not and validate the data with loaded page.
});