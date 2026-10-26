from selenium.webdriver.common.by import By


class Explore_Session_PO:

    ExploreSession_LaunchPage_Validation = (By.XPATH, "//span[text()='Explorer | Sessions']")


    def __init__(self, driver):
        self.driver = driver

    def explore_session_po_ExploreSession_LaunchPage_Validation(self):
        return self.driver.find_element(*Explore_Session_PO.ExploreSession_LaunchPage_Validation)