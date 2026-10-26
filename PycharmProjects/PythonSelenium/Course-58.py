#Frames
#frames is in main html page another html page will be embedded
#Frames can be identified , if you do all locator correct and while u run, it will fail , else u can check with developer, or in fram tag therer will be keyword call frame

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.switch_to.frame("iframe-name") #switching to frame, can give frame id attribute or frame name attribute
driver.find_element(By.LINK_TEXT,"Home").click()
driver.switch_to.default_content() # switching back to main html page
driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
time.sleep(10)