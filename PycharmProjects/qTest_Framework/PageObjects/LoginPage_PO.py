from selenium.webdriver.common.by import By

from PageObjects.HomePage_PO import HomePage_PO


class LoginPage_PO:
    username = (By.ID, "userName")
    password = (By.ID, "password")
    loginBtn = (By.ID, "loginButton")

    def __init__(self, driver):
        self.driver = driver

    def loginpage_po_username(self):
        return self.driver.find_element(*LoginPage_PO.username)

    def loginpage_po_password(self):
        return self.driver.find_element(*LoginPage_PO.password)

    def loginpage_po_loginBtn(self):
        self.driver.find_element(*LoginPage_PO.loginBtn).click()
        homepage  = HomePage_PO(self.driver)
        return homepage


