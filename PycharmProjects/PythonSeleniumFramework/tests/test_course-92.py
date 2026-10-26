#here we are seeing creating custom utilities
#whatever code we are thing , it will be reused, we can write that as method in baseclass and we can use it, instead of writing everytime
#our case explicit wait,in that explicit wait doing by link test, so we making that as method and using in our script

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
        # wait = WebDriverWait(self.driver, 10)  # explicit wait
        # wait.until(expected_conditions.presence_of_element_located(
        #     (By.XPATH, "//ul/li/a[text()='India']")))  # wait until this locator coming

        #instead of above code, we are calling the method which we written in baseclass
        str = "//ul/li/a[text()='India']"
        # str = '"//ul/li/a[text()='
        # str1 = "'India']"
        # str2 = '"'
        # str3 = str+str1+str2
        print(str)
        self.explicrwait_withlinktext(str)
        purchasepage.getloactionAppear().click()
        purchasepage.getcheckbox().click()
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()
        successMsg = purchasepage.getSuccessMsg().text
        assert "Success! Thank you!" in successMsg
        time.sleep(10)