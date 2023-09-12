# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "iOS"
caps["appium:platformVersion"] = "16.4"
caps["appium:automationName"] = "XCUITest"
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = "True"
caps["appium:nativeWebScreenshot"] = "True"
caps["appium:newCommandTimeout"] = "3600"
caps["appium:connectHardwareKeyboard"] = True
caps["appium:xcodeOrgId"] = "TAX3B9PB9G"
caps["appium:includeSafariInWebviews"] = True

driver = webdriver.Remote("http://127.0.0.1:4723", caps)


driver.quit()