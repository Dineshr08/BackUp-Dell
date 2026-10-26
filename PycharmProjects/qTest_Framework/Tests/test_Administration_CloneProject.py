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


class Test_Administration_CloneProject(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Administration_CloneProject)
    def getUserInput(self, request):
        return request.param

    # @pytest.mark.regression
    def test_Administration_CloneProject(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_User_Menu()).perform()
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.presence_of_element_located((HomePage_PO.Admin)))
            admin = homepage.homepage_po_Admin()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//label[@class='pt-1 pl-3 col-form-label filter-title no-padding-right text-nowrap']")))
            admin.admin_po_Projects().click()
            wait.until(EC.presence_of_element_located((Administration_PO.Add_New_Project)))
            self.driver.execute_script("arguments[0].click();", admin.admin_po_CloneProject())
            # admin.admin_po_AddGroups().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='projName']")))
            # time.sleep(5)
            admin.admin_po_Project_Project_Name().send_keys("AT_Project_Name_Clone")
            admin.admin_po_SourceProject().send_keys("TechOps_Validation")
            admin.admin_po_UserManagmentSetting().click()
            admin.admin_po_TestPlanStructure().click()
            admin.admin_po_Clone().click()
            wait.until(EC.element_to_be_clickable(Administration_PO.Clone_Confirmation_Yes))
            admin.admin_po_Clone_Confirmation_Yes().click()
            wait.until(EC.element_to_be_clickable(Administration_PO.Clone_Success))
            admin.admin_po_Clone_Success().click()
            wait.until(EC.presence_of_element_located((Administration_PO.Project_SearchName)))
            admin.admin_po_Project_SearchName().send_keys("AT_Project_Name_Clone")
            admin.admin_po_Project_SearchName().send_keys(Keys.ENTER)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AT_Project_Name_Clone")))
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
            self.create_TestRun(testSuiteID, 'Administration_CloneProject', '1091085')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_CloneProject')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_CloneProject', '1091085')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_CloneProject')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()














