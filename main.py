from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import time

chrome = webdriver.Chrome()
firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())


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

def codebase_find_ticket(browser):
    with open("D:\codebaseLogin.txt") as loginDetails:
        lines = loginDetails.readlines()
        url = lines[0].rstrip("\n")
        email = lines[1].rstrip("\n")
        thePassword = lines[2].rstrip("\n")
    browser.set_window_size(1482, 996)
    browser.get(url)
    username = browser.find_element(By.ID,"username")
    username.send_keys(email)
    password = browser.find_element(By.NAME,"password")
    password.send_keys(thePassword + Keys.RETURN)
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH,"//*[text()='Your Projects']").click()
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "//*[text()='Studio']").click()
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, "//*[text()='Tickets']").click()
    browser.implicitly_wait(10)
    search = browser.find_element(By.NAME,"query")
    search.send_keys("21000" + Keys.RETURN)
    browser.implicitly_wait(10)
    browser.find_element(By.LINK_TEXT,"21000").click()
    browser.implicitly_wait(10)
    assert "Cake" in browser.title
    browser.quit()

#codebase_find_ticket(firefox)
codebase_find_ticket(chrome)

#confirm_yahoo_title(firefox)
#confirm_yahoo_title(chrome)