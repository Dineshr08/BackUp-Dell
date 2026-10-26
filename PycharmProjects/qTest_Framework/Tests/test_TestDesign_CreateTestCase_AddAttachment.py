import os
import time

# import pyautogui
import pytest
# from pynput.keyboard import Controller, Key
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from TestData.LoginPage_TD import LoginPage_TD
from Utilities.BaseClass import BaseClass


class Test_TestDesign_CreateTestCase_AddAttachment(BaseClass):

    @pytest.fixture(params=LoginPage_TD.testdesign_createtestcase_addattachment)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface
    @pytest.mark.Validation


    def test_TestDesign_CreateTestCase_AddAttachment(self, getUserInput, getTSValue):
    # def test_TestDesign_CreateTestCase_AddAttachment(self, getUserInput):
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
            testdesign = homepage.homepage_po_testdesign()
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_Create_NewModule())
            # testdesign.testdesign_po_Create_NewModule().click()
            testdesign.testdesign_po_Update_NewModuleName().send_keys("AT Module")
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_CreateNewTestCase())
            # testdesign.testdesign_po_CreateNewTestCase().click()
            testdesign.testdesign_po_Update_ExistingTestCaseNameField().send_keys("AT TestCase")
            # self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_Type())
            testdesign.testdesign_po_Type().click()
            # self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_Choose_AutomationType())
            testdesign.testdesign_po_Choose_AutomationType().click()
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_Attachment())
            # testdesign.testdesign_po_Attachment().click()
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.END)
            dropzone = testdesign.testdesign_po_Upload()
            time.sleep(5)
            dropzone.drop_files("C:\\Selenium\\AT_Import.txt")
            # pyautogui.write('C:\\Selenium\\AT_Import.txt', interval=0.25)
            # pyautogui.press('return')
            # testdesign.testdesign_po_Upload().click()
            # time.sleep(5)
            # keyboard = Controller()
            # keyboard.type("C:\\Selenium\\AT_Import.txt")
            # keyboard.press(Key.enter)
            # keyboard.release(Key.enter)
            time.sleep(5)
            assert testdesign.testdesign_po_Validating_AttachmentTxt().text == "AT_Import.txt"
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_Save())
            # testdesign.testdesign_po_Save().click()
            time.sleep(10)
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_Approve())
            time.sleep(5)
            # testdesign.testdesign_po_Approve().click()
            # self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_Approve_Yes())
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Approve_Yes))
            testdesign.testdesign_po_Approve_Yes().click()
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_CreateTestCase_AddAttachment', '2681777')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_CreateTestCase_AddAttachment')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_CreateTestCase_AddAttachment', '2681777')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_CreateTestCase_AddAttachment')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()




