from selenium.webdriver.common.by import By


class PurchasePage:

    location = (By.ID, "country")
    locationappear = (By.XPATH, "//ul/li/a[text()='India']")
    checkbox = (By.CLASS_NAME, "checkbox-primary")
    purchase = (By.CLASS_NAME, "btn-success")
    succMsg = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def getloaction(self):
        return self.driver.find_element(*PurchasePage.location)

    def getloactionAppear(self):
        return self.driver.find_element(*PurchasePage.locationappear)

    def getcheckbox(self):
        return self.driver.find_element(*PurchasePage.checkbox)

    def getPurchase(self):
        return self.driver.find_element(*PurchasePage.purchase)

    def getSuccessMsg(self):
        return self.driver.find_element(*PurchasePage.succMsg)

