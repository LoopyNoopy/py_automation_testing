# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
#cd C:\Users\LocalUser\PycharmProjects\py_automation_testing\test_SGO
#pytest --alluredir=allure-results test_demo.py
#npx allure serve allure-results

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.common import AppiumOptions

def xpath_wait(driver,xpath_value, timeout = 120):
 wait = WebDriverWait(driver, timeout=timeout)  # You can adjust the timeout as needed
 try:
  element = wait.until(EC.presence_of_element_located((By.XPATH, xpath_value)))
  # Do something with the element once it is found
  print("Element found:", element.text)
 except Exception as e:
  print("Element not found within the specified time")
 return


@allure.parent_suite("Library Testing")
@allure.suite("Sign in test")
def test_signin(set_driver):
 driver = set_driver
 xpath_wait(driver,"//android.widget.Button[@text=\"Accept\"]")
 el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Accept\"]")
 el1.click()
 time.sleep(5)
 el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SkipButton")
 el2.click()
 xpath_wait(driver, "//android.widget.TextView[@text=\"Curio 2\"]")
 el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Curio 2\"]")
 el3.click()
 xpath_wait(driver,"//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton")
 el4 = driver.find_element(by=AppiumBy.XPATH,
                           value="//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton")
 el4.click()
 xpath_wait(driver,"//android.widget.TextView[@text=\"Sign in\"]")
 el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Sign in\"]")
 el5.click()
 xpath_wait(driver, "//android.widget.EditText[@text=\"Email\"]")
 el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Email\"]")
 el6.send_keys("")
 xpath_wait(driver, "//android.widget.EditText[@text=\"Password\"]")
 el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Password\"]")
 el7.send_keys("")
 xpath_wait(driver, "//android.widget.Button[@text=\"Sign In\"]")
 el8 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Sign In\"]")
 el8.click()
 xpath_wait(driver, "//*[contains(@text, 'Send')]")
 el9 = driver.find_element(by=AppiumBy.XPATH,
                           value="//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton")
 el9.click()
 xpath_wait(driver,xpath_value="//android.widget.TextView[@text=\"\"]")
 el20 = driver.find_element(by=AppiumBy.XPATH,value="//android.widget.TextView[@text=\"\"]")
 assert el20.text == ""

@allure.parent_suite("Logic Testing")
def test_failExample():
 value = 1
 assert value == 2

@allure.parent_suite("Tool Testing")
@allure.suite("Text Tool Testing")
def test_add_text(set_driver):
 driver = set_driver
 xpath_wait(driver,"//android.widget.Button[@text=\"Send\"]")
 el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Send\"]")
 el1.click()
 xpath_wait(driver,"//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton[1]")
 el2 = driver.find_element(by=AppiumBy.XPATH,
                           value="//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton[1]")
 el2.click()
 time.sleep(5)
 el3 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.TextView")
 el3.click()
 xpath_wait(driver,"//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton")
 el4 = driver.find_element(by=AppiumBy.XPATH,
                           value="//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton")
 el4.click()
 time.sleep(5)
 el5 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.view.View")
 el5.click()