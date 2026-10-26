#here we are doing object optimization
#instead of creating object for each page class in  test case or all test case , we can create object in page class file itself.
#ffor that we need to find the which locator is making integration between 2 page, need to identify that then in the page class file , need to go to that method, where we convert the locator in method, there need to pass click operation directly.
#so that locator directly have clicked then it will go to the next page, so in same method place we can create the object for that new page and need to return the object
#if we do like this instead of creating obj in multiple test case will reduce.


import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#from pageObjects.CheckoutPage import CheckoutPage1
from pageObjects.HomePage1 import HomePage1
#from pageObjects.PurchasePage import PurchasePage1
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup") calling this from baseclass
class TestFour(BaseClass):
    def test_e2e(self):#here we will keep our end 2 end test case
        # one complete end to end script
        homepage = HomePage1(self.driver)

        checkoutpage = homepage.gotoShop() #checkoutpage will hold now the obj of 2nd page, becuase we returing from there
        allProducts = checkoutpage.getallProducts()

        for products in allProducts:
            phoneName = products.find_element(By.XPATH, "div/h4/a").text
            if phoneName == "Blackberry":
                print(phoneName)
                products.find_element(By.CLASS_NAME, "btn-info").click()
                break
        checkoutpage.getclickCheckout().click()
        purchasepage = checkoutpage.getfinalcheckout() #purchasepage will hold now the obj of 3rd page, becuase we returing from there
        purchasepage.getloaction().send_keys("ind")
        wait = WebDriverWait(self.driver, 10)  # explicit wait
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//ul/li/a[text()='India']")))  # wait until this locator coming
        purchasepage.getloactionAppear().click()
        purchasepage.getcheckbox().click()
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()
        successMsg = purchasepage.getSuccessMsg().text
        assert "Success! Thank you!" in successMsg
        time.sleep(10)