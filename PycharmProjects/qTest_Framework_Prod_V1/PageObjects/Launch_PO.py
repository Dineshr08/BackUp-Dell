from selenium.webdriver.common.by import By


class Launch_PO:

    Launch_LaunchPage_Validation = (By.XPATH, "//*[name()='text' and @id='svg_1']")

    def __init__(self, driver):
        self.driver = driver

    def launch_po_Launch_LaunchPage_Validation(self):
        return self.driver.find_element(*Launch_PO.Launch_LaunchPage_Validation)