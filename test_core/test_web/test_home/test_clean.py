import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


def title_wait(driver, expected_title, timeout=120):
    wait = WebDriverWait(driver, timeout=timeout)
    try:
        wait.until(EC.title_is(expected_title))
        print(f"Title is now: {expected_title}")
    except Exception as e:
        print(f"Title is not '{expected_title}' within the specified time")
    return


@allure.story("Example landing")
def test_confirm_title(web_driver):
    title_wait(web_driver, "Home")
    assert "Home" in web_driver.title
