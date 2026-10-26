import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestPlan_PO import TestPlan_PO
from TestData.LoginPage_TD import LoginPage_TD
from Utilities.BaseClass import BaseClass


class Test_TestPlan_CreateRelease(BaseClass):

    @pytest.fixture(params=LoginPage_TD.testplan_createrelease_td)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_TestPlan_CreateRelease(self, getUserInput, getTSValue):
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
            testplan = homepage.homepage_po_testplan()
            self.driver.execute_script("arguments[0].click();", testplan.testplan_po_CreateNewRelease())
            # testplan.testplan_po_CreateNewRelease().click()
            action.move_to_element(self.driver.find_element(By.XPATH, "//span[@title='Untitled']")).send_keys(
                "ATTesting").perform()
            # testplan.testplan_po_Update_ExistingReleaseName().clear()
            # testplan.testplan_po_Update_ExistingReleaseName().send_keys("AT Testing")
            self.driver.switch_to.frame("portal_release_release_releaseDescription_editorNode_ifr")
            testplan.testplan_po_Edit_Description().send_keys("AT Description")
            self.driver.switch_to.default_content()

            # new Script
            self.driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
            testplan.testplan_po_Add().click()
            wait.until(EC.element_to_be_clickable(TestPlan_PO.Add_Requirement))
            testplan.testplan_po_Add().click()
            testplan.testplan_po_ChooseRequirement().click()
            testplan.testplan_po_Add_Requirement().click()
            assert "Link_Requirement" == testplan.testplan_po_Add_Requirement_Validation().get_attribute("innerHTML")
            element = testplan.testplan_po_Add_Attachment()
            time.sleep(5)
            element.send_keys("C:\\Selenium\\AT_Import.txt")
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='AT_Import.txt']")))
            time.sleep(10)
            assert "AT_Import.txt" == testplan.testplan_po_Add_Attachment_Validation().get_attribute("innerHTML")
            testplan.testplan_po_Save().click()
            Saved_Notifaction_Msg = testplan.testplan_po_Saved_Notification().get_attribute("innerHTML")
            assert "successfully" in Saved_Notifaction_Msg
            Created_ReleaseID = testplan.testplan_po_ReleaseID().text

            # New Build
            time.sleep(5)

            testplan.testplan_po_Build().click()
            self.driver.switch_to.frame("portal_release_build_note_editorNode_ifr")
            testplan.testplan_po_BuildNote().send_keys("AT Test")
            self.driver.switch_to.default_content()
            testplan.testplan_po_Build_Save().click()
            Saved_Notifaction_Msg1 = testplan.testplan_po_Build_Saved_Notification().get_attribute("innerHTML")
            assert "successfully" in Saved_Notifaction_Msg1
            testexecution = homepage.homepage_po_testexecution()
            Capture_All_ReleaseIDs = testexecution.testexecution_po_Get_AllReleaseID()
            All_ReleaseID = []
            for Capture_All_ReleaseID in Capture_All_ReleaseIDs:
                All_ReleaseID.append(Capture_All_ReleaseID.get_attribute("innerHTML"))
            assert Created_ReleaseID in All_ReleaseID
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestPlan_CreateRelease', '2681659')
            test_run_id = self.get_TestRun(testSuiteID, 'TestPlan_CreateRelease')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestPlan_CreateRelease', '2681659')
            test_run_id = self.get_TestRun(testSuiteID, 'TestPlan_CreateRelease')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()









