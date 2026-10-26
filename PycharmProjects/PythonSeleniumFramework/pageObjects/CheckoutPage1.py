from selenium.webdriver.common.by import By

from pageObjects.PurchasePage1 import PurchasePage1


class CheckoutPage1:

    def __init__(self, driver):
        self.driver = driver

    product = (By.XPATH, "//div[@class='card h-100']")
    phName = (By.XPATH, "div/h4/a")
    addTocart = (By.CLASS_NAME, "btn-info")
    clickCheckout = (By.CLASS_NAME, "btn-primary")
    finalcheckout = (By.CLASS_NAME, "btn-success")

    def getallProducts(self):
        return self.driver.find_elements(*CheckoutPage1.product)

    def getphoneName(self):
        return self.driver.find_element(*CheckoutPage1.phName)

    def getaddToCart(self):
        return self.driver.find_element(*CheckoutPage1.addTocart)

    def getclickCheckout(self):
        return self.driver.find_element(*CheckoutPage1.clickCheckout)

    def getfinalcheckout(self):
        self.driver.find_element(*CheckoutPage1.finalcheckout).click() #here we do click , it will go to next page, so below we are creating obj for next page and returing the obj of next page
        purchasepage = PurchasePage1(self.driver)
        return purchasepage


