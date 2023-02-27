from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

def confirm_yahoo_title(driver):
    driver.get('http://www.yahoo.com')
    time.sleep(3) # Let the user actually see something!
    driver.find_element(By.NAME,"agree").click()
    time.sleep(3) # Let the user actually see something!

    if "Yahoo" in driver.title:
        print("Yahoo is in title")
    assert 'Yahoo' in driver.title

    elem = driver.find_element(By.NAME, 'p')  # Find the search box
    elem.send_keys('Silhouette America' + Keys.RETURN)

    time.sleep(5) # Let the user actually see something!
    driver.quit()

confirm_yahoo_title(firefox)
confirm_yahoo_title(chrome)