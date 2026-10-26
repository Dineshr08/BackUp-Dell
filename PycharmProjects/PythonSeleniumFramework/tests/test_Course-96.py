#this is same as last one
#oly difference, there we passed data in tuple here we passing in dictionary

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.HomePage1 import HomePage1
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestExample7(BaseClass):

    @pytest.fixture(params=[{"name":"Dinesh","gender":"Male"},{"name":"Thilaga","gender":"Female"}])
    def getparamdata(self, request): #since we are creating fixture method inside class, need to keep self.
        return request.param

#since we have given two tuple above, it will run for 2 times
    def test_testcase4(self, getparamdata): #to use that fixture in this method, need to pass fixture methodname

        homepage = HomePage1(self.driver)
        homepage.getemail().send_keys("test@gmail.com")
        homepage.getpassword().send_keys("Password")
        homepage.getcheckbox().click()
        #creating utility for this
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Male")
        self.selectdropdown(homepage.getdropdown(),getparamdata["gender"]) #passing dictonary key data
        homepage.getname().send_keys(getparamdata["name"])#passing dictonary key data
        homepage.getradiobtn().click()
        homepage.getsubmitbtn().click()
        message = homepage.getmsg().text  # help us to get the data of ui like words in ui
        print(message)
        assert "Success" in message  # used to validate the msg, whether we are getting proper message or not
        homepage.gettwowaybox().send_keys("Dinesh R")  # (//input[@name='name'])[2] if we have multipe occurance we can give by index name
        homepage.gettwowaybox().clear()  # to clear the above performed text box
        self.driver.refresh() #here we are using this becuase the url launchig only once, since its doing from conftest
        #after completion of first iteration, the url is not launching, beacuse of that the already existed data place new data is typing
        #thatsy we are refreshing here

        time.sleep(10)