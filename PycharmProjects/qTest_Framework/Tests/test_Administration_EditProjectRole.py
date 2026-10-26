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


class Test_Administration_EditProjectRole(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Administration_EditProjectRole)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_Administration_EditProjectRole(self, getUserInput, getTSValue):
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
            admin.admin_po_FindUser().send_keys("atuser1@dell.com")
            time.sleep(2)
            admin.admin_po_FindUser().send_keys(Keys.ENTER)
            time.sleep(5)
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='atuser1@dell.com']")))
            admin.admin_po_Action().click()
            time.sleep(5)
            wait.until(EC.presence_of_element_located((Administration_PO.Edit_Project_and_Profile)))
            self.driver.execute_script("arguments[0].click();", admin.admin_po_Edit_Project_and_Profile())
            # homepage.homepage_po_Edit_Project_and_Profile().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='User Email']")))
            Current_UserProfile = admin.admin_po_Current_UserProfile().text
            # print(Current_UserProfile)
            if Current_UserProfile == "Project Admin":
                admin.admin_po_Click_User_Profile().click()
                admin.admin_po_UserProfile_Developer().click()
            elif Current_UserProfile == "Developer":
                admin.admin_po_Click_User_Profile().click()
                admin.admin_po_UserProfile_Project_Admin().click()
            admin.admin_po_UserProfile_Save().click()
            wait.until(EC.presence_of_element_located((Administration_PO.FindUser)))
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.qTest_Manager)))
            homepage.homepage_po_qTest_Manager().click()
            wait.until(EC.presence_of_element_located((By.ID, "topLeftTitle")))
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_EditProjectRole', '1089303')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_EditProjectRole')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_EditProjectRole', '1089303')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_EditProjectRole')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()











