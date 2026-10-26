#Switching window and grab text and using that text , click login
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowList = driver.window_handles #get all windows open
driver.switch_to.window(windowList[1]) #switch 1st child tab
highlightText = driver.find_element(By.XPATH,"//p[@class='im-para red']").text
print(highlightText)
time.sleep(5)
driver.close()
driver.switch_to.window(windowList[0]) #switch to parent tab
time.sleep(5)
splitData = highlightText.split(" ")
print(splitData)
for data in splitData:
    if data == 'mentor@rahulshettyacademy.com':
        driver.find_element(By.ID,"username").send_keys(data)
        driver.find_element(By.ID, "password").send_keys("Password1")
        driver.find_element(By.ID, "signInBtn").click()
        break
wait = WebDriverWait(driver, 10) #we are explicitely waiting 10 sec
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"alert-danger")))
print(driver.find_element(By.CLASS_NAME,"alert-danger").text)
time.sleep(5)

