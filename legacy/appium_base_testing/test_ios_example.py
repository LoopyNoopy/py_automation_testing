# https://appium.io/docs/en/2.0/quickstart/
# https://www.youtube.com/watch?v=0WXRYqbUMZY
# adb shell dumpsys window | find "mCurrentFocus"

import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

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
appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, caps)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_sgo(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Skip")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Curio 2")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="//XCUIElementTypeApplication[@name=\"Silhouette Go\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Sign in")
        el4.click()
        el5 = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
        el6 = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeSecureTextField")
        el7 = self.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeStaticText[@name=\"Sign In\"])[2]")
        el7.click()
        time.sleep(5)
        el8 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="//XCUIElementTypeApplication[@name=\"Silhouette Go\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeButton")
        el8.click()
        assert self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="d20@aspexsoftware.com")

    def test_assert_fail_example(self) -> None:
        value = 1
        assert value == 3
    def test_assert_success_example(self) -> None:
        value = 1
        assert value == 1

if __name__ == '__main__':
    unittest.main()
