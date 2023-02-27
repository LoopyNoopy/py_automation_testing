from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_codebase_find_ticket():
    browser = webdriver.Chrome()
    browser.set_window_size(1482, 996)
    browser.get('https://code.silhouettesoftware.com/login')
    username = browser.find_element(By.ID,"username")
    username.send_keys("dburgess@silhouettesoftware.com")
    password = browser.find_element(By.NAME,"password")
    password.send_keys("LaGqkqCQJV4F2CE" + Keys.RETURN)
    browser.find_element(By.XPATH,"//*[text()='Your Projects']").click()
    browser.find_element(By.XPATH, "//*[text()='Studio']").click()
    browser.find_element(By.XPATH, "//*[text()='Tickets']").click()
    search = browser.find_element(By.NAME,"query")
    search.send_keys("21000" + Keys.RETURN)
    browser.find_element(By.LINK_TEXT,"21000").click()
    assert "Cake" in browser.title
    browser.quit()


def test_silhouetteamerica_signin():
    browser = webdriver.Chrome()
    browser.set_window_size(1920,1080)
    browser.get('http://www.silhouetteamerica.com/')
    time.sleep(3)  # Let the user actually see something!
    browser.find_element(By.CSS_SELECTOR,'.nav-link > .material-icons-outlined').click()
    browser.quit()


def test_confirm_yahoo_title():
    browser = webdriver.Chrome()

    browser.get('http://www.yahoo.com')
    time.sleep(3) # Let the user actually see something!
    browser.find_element(By.NAME,"agree").click()
    time.sleep(3) # Let the user actually see something!
    assert 'Yahoo' in browser.title

    elem = browser.find_element(By.NAME, 'p')  # Find the search box
    elem.send_keys('Silhouette America' + Keys.RETURN)

    time.sleep(5) # Let the user actually see something!

    browser.quit()