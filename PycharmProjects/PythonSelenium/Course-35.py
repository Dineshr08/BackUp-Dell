import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
#Locators - name, id, class, xpath, css selector
driver.find_element(By.NAME,"email").send_keys("test@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Password")
driver.find_element(By.ID,"exampleCheck1").click()
#Xpath Loacator Syntax - //tagname[@attribute='Value']
#CSS Selector Loactor - tagname[attribute='value']
#for css locator , if we doing for id , we can use short cut like #id instead of above syntax
#for css locator , if we doing for classname , we can use short cut like .classname instead of above syntax
driver.find_element(By.XPATH,"//input[@name='name']").send_keys("Dinesh")
driver.find_element(By.ID,"inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR,"input[class='btn btn-success']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text #help us to get the data of ui like words in ui
print(message)
assert "Success" in message #used to validate the msg, whether we are getting proper message or not
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("Dinesh R") # (//input[@name='name'])[2] if we have multipe occurance we can give by index name
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear() # to clear the above performed text box
time.sleep(100)