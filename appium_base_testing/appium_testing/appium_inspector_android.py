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
caps["platformName"] = "Android"
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
caps["appium:automationName"] = "UIAutomator2"

driver = webdriver.Remote("http://127.0.0.1:4723", caps)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Silhouette Go")
el1.click()
print("waiting 15")
time.sleep(15)
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SkipButton")
el2.click()
print("waiting 5")
time.sleep(5)
el3 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
el3.click()
print("waiting 5")
time.sleep(5)
el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.Button[4]")
el4.click()

driver.quit()