import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture
def browser():
    # Set up desired capabilities for BrowserStack
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'
    cloud_options = {}
    cloud_options['build'] = 'my_test_build'
    cloud_options['name'] = 'my_test_name'
    options.set_capability('cloud:options',cloud_options)
    driver = webdriver.Remote('https://BROWSER_USER:BROWSER_KEY@hub-cloud.browserstack.com/wd/hub',options=options)

    yield driver

    # Cleanup after the test
    driver.quit()

def test_browserstack_search(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title
    elem = browser.find_element(By.NAME, 'q')
    #elem = browser.find_element_by_name("q")
    elem.send_keys("BrowserStack")
    elem.send_keys(Keys.RETURN)
    assert "BrowserStack" in browser.title
