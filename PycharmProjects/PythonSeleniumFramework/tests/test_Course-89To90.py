#here we are going to see about page object machenisam
#we first what we are doing is creating a new package called pageObject
#inside that folder we will have multiple class file.each class file is the ui page.for eg to complete our end to end test case , we need to gothrough 3 ui page means , we will create three class file
#in each class file which means each page, what are the locatore we are using for script, we will create as method
#then that method we will be using in our test case
#in test case we will create object for that class, then using that obj we will call that method.




import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from pageObjects.PurchasePage import PurchasePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup") calling this from baseclass
class TestFour(BaseClass):
    def test_e2e(self):#here we will keep our end 2 end test case
        # one complete end to end script
        homepage = HomePage(self.driver)
        checkoutpage = CheckoutPage(self.driver)
        purchasepage = PurchasePage(self.driver)

        homepage.gotoShop().click()
        allProducts = checkoutpage.getallProducts()

        for products in allProducts:
            phoneName = products.find_element(By.XPATH, "div/h4/a").text
            if phoneName == "Blackberry":
                print(phoneName)
                products.find_element(By.CLASS_NAME, "btn-info").click()
                break
        checkoutpage.getclickCheckout().click()
        checkoutpage.getfinalcheckout().click()
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