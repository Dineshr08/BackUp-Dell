#creating utility and implementing standards

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.HomePage1 import HomePage1
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestExample5(BaseClass):

    def test_testcase2(self):

        homepage = HomePage1(self.driver)
        homepage.getemail().send_keys("test@gmail.com")
        homepage.getpassword().send_keys("Password")
        homepage.getcheckbox().click()
        #creating utility for this
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Male")
        self.selectdropdown(homepage.getdropdown(),"Male")
        homepage.getname().send_keys("Dinesh")
        homepage.getradiobtn().click()
        homepage.getsubmitbtn().click()
        message = homepage.getmsg().text  # help us to get the data of ui like words in ui
        print(message)
        assert "Success" in message  # used to validate the msg, whether we are getting proper message or not
        homepage.gettwowaybox().send_keys("Dinesh R")  # (//input[@name='name'])[2] if we have multipe occurance we can give by index name
        homepage.gettwowaybox().clear()  # to clear the above performed text box
        time.sleep(10)

