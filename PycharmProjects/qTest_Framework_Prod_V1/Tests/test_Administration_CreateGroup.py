import time
from datetime import datetime

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


class Test_Administration_CreateGroup(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Administration_CreateGroup)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface
    def test_Administration_CreateGroup(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_User_Menu()).perform()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((HomePage_PO.Admin)))
            admin = homepage.homepage_po_Admin()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//label[@class='pt-1 pl-3 col-form-label filter-title no-padding-right text-nowrap']")))
            admin.admin_po_Groups().click()
            wait.until(EC.presence_of_element_located((Administration_PO.AddGroups)))
            self.driver.execute_script("arguments[0].click();", admin.admin_po_AddGroups())
            # admin.admin_po_AddGroups().click()
            Date = datetime.now()
            name = "AT_Custom_Group" + str(Date)
            admin.admin_po_Group_GroupName().send_keys(name)
            wait.until(EC.presence_of_element_located((Administration_PO.Group_Permission_InightEditor)))
            admin.admin_po_Group_Permission_InightViewer().click()
            admin.admin_po_Group_Permission_InightEditor().click()
            admin.admin_po_Groups_Users().click()
            time.sleep(20)
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Name']")))
            admin.admin_po_Groups_Users_Search().send_keys("ptuser20")
            admin.admin_po_Groups_Users_Search().send_keys(Keys.ENTER)
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='pt user20']")))
            self.driver.execute_script("arguments[0].click();", admin.admin_po_Groups_Users_SelectAllCheckBox())
            # admin.admin_po_Groups_Users_SelectAllCheckBox().click()
            admin.admin_po_Group_User_Add().click()
            admin.admin_po_Group_Save().click()
            assert "success" in admin.admin_po_Group_Creation_Validation().get_attribute("innerHTML")
            # admin.admin_po_Find_Group().send_keys("AT_Custom_Group")
            # admin.admin_po_Find_Group().send_keys(Keys.ENTER)
            # wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='AT_Custom_Group']")))
            # admin.admin_po_Group_Custom_Group_Action().click()
            # admin.admin_po_Group_Delete().click()
            # admin.admin_po_Group_Delete_Yes().click()
            # assert admin.admin_po_Group_Deletion_Validation().text in "deleted"
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.qTest_Manager)))
            homepage.homepage_po_qTest_Manager().click()
            wait.until(EC.presence_of_element_located((By.ID, "topLeftTitle")))
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_CreateGroup', '1091084')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_CreateGroup')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_CreateGroup', '1091084')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_CreateGroup')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()














