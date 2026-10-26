#Switching back to child and parent window
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Click Here").click()
#get the list of window open and store in list
windowsOpened = driver.window_handles # windowsOpened will have all opened window in order
#Switching to child window
driver.switch_to.window(windowsOpened[1]) # switching to child window
child = driver.find_element(By.TAG_NAME,"h3").text
assert child == "New Window"
time.sleep(10)
driver.close() #close the child window
#Switching back to parent window
driver.switch_to.window(windowsOpened[0]) # switching to parent window
parent = driver.find_element(By.TAG_NAME,"h3").text
assert parent == "Opening a new window"
time.sleep(10)