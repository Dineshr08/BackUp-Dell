#in this course what we have seen is, continuation of last course standardization
#in conftest file we kept browser invocation code fixture, but we have issue ther till now code was like below

# @pytest.fixture(scope="class")
# def setup():
#     service_obj = Service("C:\Selenium\chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     driver.get("https://rahulshettyacademy.com/angularpractice/")

#but our objective is to keep yield st to close the browser and want to return the driver too , so that we can access that driver obj in test case method.
#but we have problem while doing that, keeping return and yield in next to next it wont work, so we are modifing below code


# @pytest.fixture(scope="class")
# def setup():
#     service_obj = Service("C:\Selenium\chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     return driver
#     yield
#     driver.close()

#modified code, what here we are doing is, request is the instance variable of setup, so using that request connecting this fixture to fixtur we pass in clas "@pytest.mark.usefixtures("setup")"
#so here what we are doing is request.cls.driver = driver , our local driver we are passing class driver.whenever in the class the fixture is called the class driver variable will take which hold the local driver details.
#so we are calling driver in method, all class variable should be called as self.class variable name ir self.driver will be used in method
#so we no need to use return driver statement now
#if it confuse pls watch vide once
#better remember request.cls.driver = driverthis instead of return driver and in testcase method use self.driver

# @pytest.fixture(scope="class")
# def setup(request):
#     service_obj = Service("C:\Selenium\chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     request.cls.driver = driver
#     yield
#     driver.close()

#then here we learned about utilities
#creating one python package called utlities, inside that we have Clkass called BaseClass
#in that base class we have commenly used coded across all test cases
#in our case @pytest.mark.usefixtures("setup") which will passed across all the test case, instead of writing this in alll test case we have created base class wand writted that.that base class will hold this property.
#so we can directly inherit that base class to our test case, so everytime we no need to write this



import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup") calling this from baseclass
class TestThree(BaseClass):
    def test_e2e(self):#here we will keep our end 2 end test case
        # one complete end to end script

        self.driver.find_element(By.LINK_TEXT, "Shop").click()
        allProducts = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for products in allProducts:
            phoneName = products.find_element(By.XPATH, "div/h4/a").text
            if phoneName == "Blackberry":
                print(phoneName)
                products.find_element(By.CLASS_NAME, "btn-info").click()
                break
        self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)  # explicit wait
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//ul/li/a[text()='India']")))  # wait until this locator coming
        self.driver.find_element(By.XPATH, "//ul/li/a[text()='India']").click()
        self.driver.find_element(By.CLASS_NAME, "checkbox-primary").click()
        self.driver.find_element(By.CLASS_NAME, "btn-success").click()
        successMsg = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successMsg
        time.sleep(10)
