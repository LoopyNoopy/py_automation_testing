import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def element_wait(mobile_driver, by_type, finder_value, timeout=120):
    wait = WebDriverWait(mobile_driver, timeout=timeout)
    try:
        element = wait.until(EC.presence_of_element_located((by_type, finder_value)))
        print("Element found:", element.text)
    except Exception as e:
        print("Element not found within the specified time")
    return
