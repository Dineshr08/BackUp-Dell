from selenium.webdriver.common.by import By


class HomePage:

    shop = (By.LINK_TEXT, "Shop") #have the locater inside tuple

    def __init__(self, driver): #this driver we are getting from testcase, where we will create a object for the class and pass driver as argument, so it can be accessible here
        self.driver = driver

    def gotoShop(self):
        return self.driver.find_element(*HomePage.shop) # calling HomePage.shop herew because shop is class variable so class var  has to call like this and we are passing that value here
        #using * here because python wil automatically make tuple value into driver.find_element input
        #self.driver.find_element(By.LINK_TEXT, "Shop").click() we are cobstructing this statement to like above, so whenever there is change in locatore, directly we can change here insted of each scripts
