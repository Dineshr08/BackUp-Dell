from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    product = (By.XPATH, "//div[@class='card h-100']")
    phName = (By.XPATH, "div/h4/a")
    addTocart = (By.CLASS_NAME, "btn-info")
    clickCheckout = (By.CLASS_NAME, "btn-primary")
    finalcheckout = (By.CLASS_NAME, "btn-success")

    def getallProducts(self):
        return self.driver.find_elements(*CheckoutPage.product)

    def getphoneName(self):
        return self.driver.find_element(*CheckoutPage.phName)

    def getaddToCart(self):
        return self.driver.find_element(*CheckoutPage.addTocart)

    def getclickCheckout(self):
        return self.driver.find_element(*CheckoutPage.clickCheckout)

    def getfinalcheckout(self):
        return self.driver.find_element(*CheckoutPage.finalcheckout)


