#one complete end to end script
# to validate x path in console $x("")
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
allProducts = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for products in allProducts:
    phoneName = products.find_element(By.XPATH,"div/h4/a").text
    if phoneName == "Blackberry":
        print(phoneName)
        products.find_element(By.CLASS_NAME,"btn-info").click()
        break
driver.find_element(By.CLASS_NAME,"btn-primary").click()
driver.find_element(By.CLASS_NAME,"btn-success").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)#explicit wait
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//ul/li/a[text()='India']"))) #wait until this locator coming
driver.find_element(By.XPATH,"//ul/li/a[text()='India']").click()
driver.find_element(By.CLASS_NAME,"checkbox-primary").click()
driver.find_element(By.CLASS_NAME,"btn-success").click()
successMsg = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successMsg
time.sleep(10)
driver.close()