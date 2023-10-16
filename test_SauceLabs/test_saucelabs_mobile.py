from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

def test_sgo():
    options = AppiumOptions()
    caps = {}
    caps['platformName'] = 'Android'
    caps['appium:app'] = 'storage:filename=com.SilhouetteSoftware.SilhouetteGo.apk'
    caps['appium:deviceName'] = 'Android GoogleAPI Emulator'
    caps['appium:platformVersion'] = '12.0'
    caps['appium:automationName'] = 'UiAutomator2'
    caps['sauce:options'] = {}
    caps['sauce:options']['username'] = ''
    caps['sauce:options']['accessKey'] = ''
    caps['sauce:options']['build'] = 'appium-build-S612M'
    caps['sauce:options']['name'] = '<your test name>'
    caps['sauce:options']['deviceOrientation'] = 'PORTRAIT'

    options.load_capabilities(caps)

    url = 'https://ondemand.eu-central-1.saucelabs.com:443/wd/hub'
    driver = webdriver.Remote(url, options=options)

    el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SkipButton")
    el1.click()