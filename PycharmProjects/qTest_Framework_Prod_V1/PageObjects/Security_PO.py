from selenium.webdriver.common.by import By


class Security_PO:

    PasswordPeriod = (By.ID, "passwordHealthyPeriod")
    PasswordLife = (By.ID, "passwordShelfLife")
    DistinctPassword = (By.ID, "minimumUniquePasswordsSequenceLength")
    FailedLoginAttempt = (By.ID, "maxFailedLoginAttempt")
    AccessTokenExpiry = (By.ID, "accessTokenTimeout")
    RefreshTokenExpiry = (By.ID, "refreshTokenTimeout")
    PasswordLength = (By.ID, "minimumPasswordLength")


    def __init__(self, driver):
        self.driver = driver

    def security_po_PasswordPeriod(self):
        return self.driver.find_element(*Security_PO.PasswordPeriod)

    def security_po_PasswordLife(self):
        return self.driver.find_element(*Security_PO.PasswordLife)

    def security_po_DistinctPassword(self):
        return self.driver.find_element(*Security_PO.DistinctPassword)

    def security_po_FailedLoginAttempt(self):
        return self.driver.find_element(*Security_PO.FailedLoginAttempt)

    def security_po_AccessTokenExpiry(self):
        return self.driver.find_element(*Security_PO.AccessTokenExpiry)

    def security_po_RefreshTokenExpiry(self):
        return self.driver.find_element(*Security_PO.RefreshTokenExpiry)

    def security_po_PasswordLength(self):
        return self.driver.find_element(*Security_PO.PasswordLength)