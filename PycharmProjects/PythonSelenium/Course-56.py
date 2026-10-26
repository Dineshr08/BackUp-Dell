#ActionChains class - which is used to perform action like hover the mouse, souble click, drag and drop, right click etc
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
action = ActionChains(driver) #using this call so we can perform above mention comment steps
#action.click_and_hold() just to clikc and hold
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform() #hovering and whenever using ActionChains at end need to call .perform() fn
#we can use click or send key operations in ActionChains class like below
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(10)
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform() #right click
time.sleep(10)