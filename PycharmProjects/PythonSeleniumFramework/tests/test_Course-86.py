#this is the continuation of previous course, standardizing framework
#while doing standardization, first thing is browser invocation is comman for all test cases, so we are keep that in fixture by creating conftest file
#so we can use that across all testcases

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestTwo:
    def test_e2e(self):#here we will keep our end 2 end test case
        # one complete end to end script

        driver.find_element(By.LINK_TEXT, "Shop").click()
        allProducts = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for products in allProducts:
            phoneName = products.find_element(By.XPATH, "div/h4/a").text
            if phoneName == "Blackberry":
                print(phoneName)
                products.find_element(By.CLASS_NAME, "btn-info").click()
                break
        driver.find_element(By.CLASS_NAME, "btn-primary").click()
        driver.find_element(By.CLASS_NAME, "btn-success").click()
        driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(driver, 10)  # explicit wait
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//ul/li/a[text()='India']")))  # wait until this locator coming
        driver.find_element(By.XPATH, "//ul/li/a[text()='India']").click()
        driver.find_element(By.CLASS_NAME, "checkbox-primary").click()
        driver.find_element(By.CLASS_NAME, "btn-success").click()
        successMsg = driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successMsg
        time.sleep(10)
        driver.close()
