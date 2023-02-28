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

def codebase_find_ticket(browser):
    browser.set_window_size(1482, 996)
    browser.get('https://code.silhouettesoftware.com/login')
    username = browser.find_element(By.ID,"username")
    username.send_keys("dburgess@silhouettesoftware.com")
    password = browser.find_element(By.NAME,"password")
    password.send_keys("LaGqkqCQJV4F2CE" + Keys.RETURN)
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
confirm_yahoo_title(chrome)