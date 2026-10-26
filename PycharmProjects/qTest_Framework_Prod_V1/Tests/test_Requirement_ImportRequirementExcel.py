import time
import pytest
# from pynput.keyboard import Controller, Key
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.LoginPage_PO import LoginPage_PO
from TestData.LoginPage_TD import LoginPage_TD
from Utilities.BaseClass import BaseClass


class Test_Requirement_ImportRequirementExcel(BaseClass):

    @pytest.fixture(params=LoginPage_TD.requirement_importrequirementexcel)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_Requirement_ImportRequirementExcel(self, getUserInput, getTSValue):
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
            self.driver.execute_script("arguments[0].click();", requirement.requirement_po_ImportExcel_Icon())
            # requirement.requirement_po_ImportExcel_Icon().click()
            element = requirement.requirement_po_ChooseFile_Hyperlink()
            element.send_keys("C:\\Selenium\\Import.xls")
            # requirement.requirement_po_ChooseFile_Hyperlink().click()
            # time.sleep(5)
            # keyboard = Controller()
            # keyboard.type("C:\\Selenium\\Import.xls")
            # keyboard.press(Key.enter)
            # keyboard.release(Key.enter)
            # time.sleep(5)
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Import.xls']")))
            time.sleep(10)
            self.driver.execute_script("arguments[0].click();", requirement.requirement_po_Import_Next())
            # requirement.requirement_po_Import_Next().click()
            # ----Disabling , since data getting updated by default
            # RequirementName_Source = requirement.requirement_po_Import_RequirementName_Source()
            # RequirementName_Destination = requirement.requirement_po_Import_RequirementName_Destination()
            # action.drag_and_drop(RequirementName_Source, RequirementName_Destination).perform()
            # Status_Source = requirement.requirement_po_Import_Status_Source()
            # Status_Destination = requirement.requirement_po_Import_Status_Destination()
            # action.drag_and_drop(Status_Source, Status_Destination).perform()
            # self.driver.execute_script("arguments[0].click();", requirement.requirement_po_Import_Excel())
            requirement.requirement_po_Import_Excel().click()
            wait.until(EC.presence_of_element_located((By.ID, "successImportMessageRequirement")))
            Imported_Notifaction_Msg = requirement.requirement_po_ImportSuccess_PopUp().get_attribute("innerHTML")
            assert "Your file(s) have been imported successfully!" in Imported_Notifaction_Msg
            # self.driver.execute_script("arguments[0].click();", requirement.requirement_po_Import_OK())
            requirement.requirement_po_Import_OK().click()
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Requirement_ImportRequirementExcel', '2681781')
            test_run_id = self.get_TestRun(testSuiteID, 'Requirement_ImportRequirementExcel')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Requirement_ImportRequirementExcel', '2681781')
            test_run_id = self.get_TestRun(testSuiteID, 'Requirement_ImportRequirementExcel')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()

