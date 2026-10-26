import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.Requirement_PO import Requirement_PO
from TestData.LoginPage_TD import LoginPage_TD
from Utilities.BaseClass import BaseClass


class Test_Requirement_CreateModule_and_Requirement_LinkTestCase(BaseClass):

    @pytest.fixture(params=LoginPage_TD.requirement_createmodule_and_requirement_linktestCase)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface



    def test_Requirement_CreateModule_and_Requirement_LinkTestCase(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_hoverProjectMenu()).perform()
            homepage.homepage_po_searchProject().send_keys("Automation")
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting")))
            time.sleep(5)
            homepage.homepage_po_chooseATProject().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting']")))
            UI_LandingPage_Validation = homepage.homepage_po_ATProject_landingPage_Validation().text
            assert "AutomationTesting" == UI_LandingPage_Validation
            requirement = homepage.homepage_po_requirement()
            time.sleep(5)
            for i in range(2):
                requirement.requirement_po_New_Module().click()
                if i == 0:
                    requirement.requirement_po_Update_New_Module_Name().send_keys("AT Module")
                elif i == 1:
                    requirement.requirement_po_Update_New_Module_Name().send_keys("AT SubModule")

            time.sleep(5)
            requirement.requirement_po_New_Requirement().click()
            # time.sleep(5)
            # self.driver.find_element(By.XPATH, "(//span[text()='Untitled'])[last()]").click()
            # requirement.requirement_po_Update_ExistingRequirementName().clear()
            # requirement.requirement_po_Update_ExistingRequirementName().send_keys("AT Requirement")
            time.sleep(6)
            requirement.requirement_po_Status().clear()
            time.sleep(5)
            requirement.requirement_po_Status().send_keys("In Progress")
            time.sleep(5)
            requirement.requirement_po_Priority().clear()
            time.sleep(5)
            requirement.requirement_po_Priority().send_keys("Nice to Have")
            time.sleep(5)
            requirement.requirement_po_AddBtn().click()
            time.sleep(5)
            requirement.requirement_po_ChooseModule_LinkTestCase().click()
            time.sleep(5)
            requirement.requirement_po_ChooseModule_LinkTestCase_Expand().click()
            time.sleep(5)
            requirement.requirement_po_ChooseModule_LinkTestCase_SelectTestCase().click()
            time.sleep(5)
            requirement.requirement_po_Add_LinkTestCase().click()
            time.sleep(5)
            requirement.requirement_po_Save().click()
            time.sleep(5)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[contains(text(),'Changes were saved successfully.')]")))
            Saved_Notifaction_Msg = requirement.requirement_po_Saved_Notification().get_attribute("innerHTML")
            assert "successfully" in Saved_Notifaction_Msg
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Requirement_CreateModule_and_Requirement_LinkTestCase', '2681775')
            test_run_id = self.get_TestRun(testSuiteID, 'Requirement_CreateModule_and_Requirement_LinkTestCase')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Requirement_CreateModule_and_Requirement_LinkTestCase', '2681775')
            test_run_id = self.get_TestRun(testSuiteID, 'Requirement_CreateModule_and_Requirement_LinkTestCase')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()