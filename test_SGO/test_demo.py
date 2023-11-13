# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
#cd C:\Users\LocalUser\PycharmProjects\py_automation_testing\test_SGO
#pytest --alluredir=allure-results test_demo.py
#npx allure serve allure-results

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.common import AppiumOptions

def test_signin():
 options = AppiumOptions()
 caps = {}
 caps["platformName"] = "Android"
 caps["appium:platformVersion"] = "11"
 caps["appium:automationName"] = "UIAutomator2"
 caps["appium:noReset"] = True
 caps["appium:ensureWebviewsHavePages"] = True
 caps["appium:nativeWebScreenshot"] = True
 caps["appium:newCommandTimeout"] = 3600
 caps["appium:connectHardwareKeyboard"] = True

 options.load_capabilities(caps)

 driver = webdriver.Remote("http://127.0.0.1:4725", options=options)

 el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Silhouette Go")
 el1.click()
 time.sleep(10)
 el1 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Accept\"]")
 el1.click()
 time.sleep(1)
 el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SkipButton")
 el2.click()
 time.sleep(1)
 el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Curio 2\"]")
 el3.click()
 time.sleep(1)
 el4 = driver.find_element(by=AppiumBy.XPATH,
                           value="//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton")
 el4.click()
 time.sleep(1)
 el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Sign in\"]")
 el5.click()
 time.sleep(1)
 el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Email\"]")
 el6.send_keys("d20@aspexsoftware.com")
 time.sleep(1)
 el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text=\"Password\"]")
 el7.send_keys("12345")
 time.sleep(1)
 el8 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Sign In\"]")
 el8.click()
 time.sleep(15)
 el9 = driver.find_element(by=AppiumBy.XPATH,
                           value="//androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageButton")
 el9.click()
 time.sleep(1)
 el20 = driver.find_element(by=AppiumBy.XPATH,value="//android.widget.TextView[@text=\"d20@aspexsoftware.com\"]")
 assert el20.text == "d20@aspexsoftware.com"

 driver.quit()

def test_failExample():
 value = 1
 assert value == 2