#in this course what we are seeing is, how to write log to html report and when error come how to get screenshot and automatically put in report
#for getting screen shot of failure, need to have already existing method in conftest file and need to keep driver  = None at top of the file then keep global driver in browser invocation method in same conftest file
#why we are doing this is, in get screenshot method(existing method whcih we keep in conftest file) which has driver and it dose not have any connection to main driver which has in browser invocation
#by doing above way, first driver will be none, then when browser invocation happend that time that driver will become global driver, so all the other method mainly screenshot method driver now have access to that

#from above , just one change , need to remove driver  = None at the top
#best practise always keep logfile in utilities flder and screenshots and report in test folder
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from TestData.HomePageTestdata import HomepageTestData
from pageObjects.HomePage1 import HomePage1
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestExample9(BaseClass):

    @pytest.fixture(params=HomepageTestData.testdata_homepage) #getting data from TestData package and pass to this testcase
    def getparamdata(self, request): #since we are creating fixture method inside class, need to keep self.
        return request.param

#since we have given two tuple above, it will run for 2 times
    def test_testcase6(self, getparamdata): #to use that fixture in this method, need to pass fixture methodname

        log = self.logging() #calling logging method and assigning to log obj

        homepage = HomePage1(self.driver)
        homepage.getemail().send_keys("test@gmail.com")
        homepage.getpassword().send_keys("Password")
        homepage.getcheckbox().click()
        #creating utility for this
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropdown.select_by_visible_text("Male")
        self.selectdropdown(homepage.getdropdown(),getparamdata["gender"]) #passing dictonary key data
        log.info(getparamdata["gender"])
        homepage.getname().send_keys(getparamdata["name"])#passing dictonary key data
        log.info(getparamdata["name"])
        homepage.getradiobtn().click()
        homepage.getsubmitbtn().click()
        message = homepage.getmsg().text  # help us to get the data of ui like words in ui
        #print(message)
        log.info(message)
        assert "Succ2222ess" in message #explicitly making this text to fail to getscreenshot
        homepage.gettwowaybox().send_keys("Dinesh R")  # (//input[@name='name'])[2] if we have multipe occurance we can give by index name
        homepage.gettwowaybox().clear()  # to clear the above performed text box
        time.sleep(10)
        self.driver.refresh() #here we are using this becuase the url launchig only once, since its doing from conftest
        #after completion of first iteration, the url is not launching, beacuse of that the already existed data place new data is typing
        #thatsy we are refreshing here