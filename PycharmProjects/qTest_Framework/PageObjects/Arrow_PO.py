from selenium.webdriver.common.by import By


class Arrow_PO:

    CI_ToolIntegartion = (By.XPATH, "//span[text()='CI Tool Integration']")
    API_SDK = (By.XPATH, "//span[text()='API & SDK']")
    Jenkin_RefreshToken = (By.ID, "jenkins-refresh-token")
    API_BearerToken = (By.ID, "user-access-token")
    API_Token = (By.ID, "legacy-user-access-token")

    def __init__(self, driver):
        self.driver = driver

    def arrow_po_CI_ToolIntegartion(self):
        return self.driver.find_element(*Arrow_PO.CI_ToolIntegartion)

    def arrow_po_API_SDK(self):
        return self.driver.find_element(*Arrow_PO.API_SDK)

    def arrow_po_Jenkin_RefreshToken(self):
        return self.driver.find_element(*Arrow_PO.Jenkin_RefreshToken)

    def arrow_po_API_BearerToken(self):
        return self.driver.find_element(*Arrow_PO.API_BearerToken)

    def arrow_po_API_Token(self):
        return self.driver.find_element(*Arrow_PO.API_Token)