import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Administration_PO import Administration_PO
from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_Administration_CreateProject(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Administration_CreateProject)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_Administration_CreateProject(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_User_Menu()).perform()
            wait = WebDriverWait(self.driver, 120)
            wait.until(EC.presence_of_element_located((HomePage_PO.Admin)))
            admin = homepage.homepage_po_Admin()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//label[@class='pt-1 pl-3 col-form-label filter-title no-padding-right text-nowrap']")))
            admin.admin_po_Projects().click()
            wait.until(EC.presence_of_element_located((Administration_PO.Add_New_Project)))
            self.driver.execute_script("arguments[0].click();", admin.admin_po_Add_New_Project())
            # admin.admin_po_AddGroups().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='projName']")))
            # time.sleep(5)
            admin.admin_po_Project_Project_Name().send_keys("AT_Project_Name")
            # admin.admin_po_Project_Template().send_keys("Sample Site Field Template")
            admin.admin_po_Project_Template().send_keys("Base Template")
            # admin.admin_po_Project_Template().send_keys(Keys.ENTER)
            admin.admin_po_Project_Add().click()
            wait.until(EC.element_to_be_clickable((Administration_PO.Project_OK)))
            admin.admin_po_Project_OK().click()
            wait.until(EC.presence_of_element_located((Administration_PO.Project_SearchName)))
            admin.admin_po_Project_SearchName().send_keys("AT_Project_Name")
            admin.admin_po_Project_SearchName().send_keys(Keys.ENTER)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AT_Project_Name")))
            # time.sleep(3)
            # admin.admin_po_Project_Delete().click()
            # time.sleep(3)
            # admin.admin_po_Project_Delete_Yes().click()
            # time.sleep(3)
            # wait.until(EC.invisibility_of_element_located((By.LINK_TEXT, "AT_Project_Name")))
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.qTest_Manager)))
            homepage.homepage_po_qTest_Manager().click()
            wait.until(EC.presence_of_element_located((By.ID, "topLeftTitle")))
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_CreateProject', '1091085')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_CreateProject')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_CreateProject', '1091085')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_CreateProject')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()














