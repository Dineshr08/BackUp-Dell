from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage1 import CheckoutPage1


class HomePage1:

    shop = (By.LINK_TEXT, "Shop") #have the locater inside tuple
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    name = (By.XPATH, "//input[@name='name']")
    radiobtn = (By.ID, "inlineRadio1")
    submitbtn = (By.CSS_SELECTOR, "input[class='btn btn-success']")
    msg = (By.CLASS_NAME, "alert-success")
    twowaybox = (By.XPATH, "(//input[@name='name'])[2]")
    dropdown = (By.ID, "exampleFormControlSelect1")


    def __init__(self, driver): #this driver we are getting from testcase, where we will create a object for the class and pass driver as argument, so it can be accessible here
        self.driver = driver

    def gotoShop(self):
        self.driver.find_element(*HomePage1.shop).click() #here we do click , it will go to next page, so below we are creating obj for next page and returing the obj of next page
        checkoutpage = CheckoutPage1(self.driver)
        return checkoutpage

    def getemail(self):
        return self.driver.find_element(*HomePage1.email)

    def getpassword(self):
        return self.driver.find_element(*HomePage1.password)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage1.checkbox)

    def getname(self):
        return self.driver.find_element(*HomePage1.name)

    def getradiobtn(self):
        return self.driver.find_element(*HomePage1.radiobtn)

    def getsubmitbtn(self):
        return self.driver.find_element(*HomePage1.submitbtn)

    def getmsg(self):
        return self.driver.find_element(*HomePage1.msg)

    def gettwowaybox(self):
        return self.driver.find_element(*HomePage1.twowaybox)

    def getdropdown(self):
        return self.driver.find_element(*HomePage1.dropdown)

