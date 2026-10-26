#Gng to see other different locator, link text, parent child xpath and css, then xpath using button name
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
#Link text - it start with tag name a then only can use this
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
#Xpath - PArent Child obtaining  //form/div[1]/input - no need to give attribut that is optional only for regular or parent child xpath
#some time we wont have any attribute in html page that time this parent child will help
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demotest@gmail.com")
#Css - PArent Child obtaining  form div:nth-child(2) input - no need to give attribut that is optional only for regular or parent child xpath
#some time we wont have any attribute in html page that time this parent child will help
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Password@2")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(3) input").send_keys("Password@2")
#Xpath  -  using button name
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
time.sleep(100)

