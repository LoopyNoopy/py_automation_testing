import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture
def browser():
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 11'
    sauce_options = {}
    sauce_options['username'] = ''
    sauce_options['accessKey'] = ''
    sauce_options['build'] = 'selenium-build-0LC36'
    sauce_options['name'] = '<your test name>'
    options.set_capability('sauce:options', sauce_options)

    url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=options)

    yield driver

    # Cleanup after the test
    driver.quit()

def test_saucelabs_search(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title
    elem = browser.find_element(By.NAME, 'q')
    #elem = browser.find_element_by_name("q")
    elem.send_keys("Chicken nuggets")
    elem.send_keys(Keys.RETURN)
    assert "Chicken nuggets" in browser.title

