#Alert or pop up, in our app if pop up or alert comes, how to handle it
# usually the popup or alert wont be html page, it will be java or javascript.java or java script cant handle by selenium driver.
#for that  we need to move to alert mode
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"name").send_keys("Tamil")
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert # here we are getting alert or popup , so we are moving to alert mode
alerttext  = alert.text # getting alert text
print(alerttext)
assert "Tamil" in alerttext #checking whether we are getting alert , by the word we are enetering
time.sleep(10)
alert.accept() # clicking ok
#alert.dismiss() #clicking cancel

time.sleep(10)