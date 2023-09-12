# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "iOS"
caps["appium:platformVersion"] = "16.5.1"
caps["appium:udid"] = "00008112-001548503487401E"
caps["appium:automationName"] = "XCUITest"
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = "3600"
caps["appium:connectHardwareKeyboard"] = True
caps["appium:xcodeOrgId"] = "TAX3B9PB9G"
caps["AddAdditionalCapability:app"] = "/Users/XXXX/abcd.app"
caps["appium:includeSafariInWebviews"] = True

driver = webdriver.Remote("http://127.0.0.1:4723", caps)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Skip")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Curio 2")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeApplication[@name=\"Silhouette Go\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton")
el3.click()
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sign in")
el4.click()
el5 = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
el6 = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeSecureTextField")
el7 = driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeStaticText[@name=\"Sign In\"])[2]")
el7.click()
time.sleep(5)
el8 = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeApplication[@name=\"Silhouette Go\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton")
el8.click()

driver.quit()