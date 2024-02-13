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
caps["platformName"] = "Android"
caps["appium:platformVersion"] = "13"
caps["appium:deviceName"] = "Pixel 5"
caps["appium:automationName"] = "UIAutomator2"
caps["appium:noReset"] = True
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True
appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, caps)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_sgo(self) -> None:
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SkipButton")
        el1.click()
        time.sleep(15)
        el2 = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el2.click()
        time.sleep(5)
        el3 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText")
        el3.send_keys("d20@aspexsoftware.com")
        time.sleep(5)
        el4 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
        el4.send_keys("12345")
        time.sleep(5)
        el5 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.Button[2]")
        el5.click()
        time.sleep(30)
        el6 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView")
        el6.click()
        time.sleep(5)
        el6.click()
        time.sleep(5)
        el6.click()
        time.sleep(5)
        el6.click()
        time.sleep(5)
        el10 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.view.ViewGroup/android.widget.TextView")
        el10.click()
        time.sleep(15)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(527, 830)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(5)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(690, 1007)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(860, 1171)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(5)

        el11 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.Button")
        el11.click()
        time.sleep(5)
        el12 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.Button")
        el12.click()
        time.sleep(5)
        el13 = self.driver.find_element(by=AppiumBy.ID, value="android:id/search_src_text")
        el13.send_keys("vinyl")
        time.sleep(5)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(153, 986)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(0.1)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(5)
        el14 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView")
        el14.click()
        time.sleep(5)
        el15 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.Button")
        el15.click()
        time.sleep(5)
        el16 = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el16.click()
        time.sleep(5)
        el17 = self.driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el17.click()
        time.sleep(5)
        el18 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SkipButton")
        el18.click()
        time.sleep(5)
        el19 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.FrameLayout")
        el19.click()
        time.sleep(5)
        el20 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.FrameLayout")
        el20.click()
        time.sleep(5)
        el21 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.FrameLayout")
        el21.click()
        time.sleep(5)
        el22 = self.driver.find_element(by=AppiumBy.XPATH,
                                   value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.Button")
        el22.click()


if __name__ == '__main__':
    unittest.main()
