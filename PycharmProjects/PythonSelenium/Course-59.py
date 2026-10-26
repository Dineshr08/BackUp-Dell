#How to run java scripts
#how to take screen shots
#how to run in headless mode ie in chrome in backend
#how to ignore cretificate errors

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#making chrome to run headless
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless") #making chrome to run headless
#making chrome to ignore certificates
chromeOptions.add_argument("--ignore-certificate-errors")
service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chromeOptions) #making chrome to run headless AND Ignore certificates
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.execute_script("window.scrollBy(0,700);") # used to execute javascript, it will scroll till 700 length
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") #used to come to bottom
driver.get_screenshot_as_file("screenshot1.png") # get screenshot of current page