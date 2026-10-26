from selenium.webdriver.common.by import By


class PurchasePage1:

    location = (By.ID, "country")
    locationappear = (By.XPATH, "//ul/li/a[text()='India']")
    checkbox = (By.CLASS_NAME, "checkbox-primary")
    purchase = (By.CLASS_NAME, "btn-success")
    succMsg = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def getloaction(self):
        return self.driver.find_element(*PurchasePage1.location)

    def getloactionAppear(self):
        return self.driver.find_element(*PurchasePage1.locationappear)

    def getcheckbox(self):
        return self.driver.find_element(*PurchasePage1.checkbox)

    def getPurchase(self):
        return self.driver.find_element(*PurchasePage1.purchase)

    def getSuccessMsg(self):
        return self.driver.find_element(*PurchasePage1.succMsg)

