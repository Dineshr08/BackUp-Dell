#Sorting the webtables and check the table sorted properly
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.LINK_TEXT,"Top Deals").click()
#Table sorting
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
sortedListelement = driver.find_elements(By.XPATH,"//tr/td[1]")
time.sleep(5)
webTableSortedListElement = []
for element in sortedListelement:
    webTableSortedListElement.append(element.text)
driver.close()
driver.switch_to.window(windowsOpened[0])
webTableSortedListElementOrginal = webTableSortedListElement.copy() #copy list to new list
#sorting the list
webTableSortedListElement.sort()
assert webTableSortedListElementOrginal == webTableSortedListElement
time.sleep(5)