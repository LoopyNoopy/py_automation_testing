from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

def test_codebase_find_ticket():
    with open("D:\codebaseLogin.txt") as loginDetails:
        lines = loginDetails.readlines()
        url = lines[0].rstrip("\n")
        email = lines[1].rstrip("\n")
        thePassword = lines[2].rstrip("\n")
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.set_window_size(1482, 996)
    browser.get(url)
    browser.implicitly_wait(30)
    username = browser.find_element(By.ID,"username")
    username.send_keys(email)
    browser.implicitly_wait(30)
    password = browser.find_element(By.NAME,"password")
    password.send_keys(thePassword + Keys.RETURN)
    browser.implicitly_wait(30)
    browser.find_element(By.XPATH,"//*[text()='Your Projects']").click()
    browser.implicitly_wait(30)
    browser.find_element(By.XPATH, "//*[text()='Studio']").click()
    browser.implicitly_wait(30)
    browser.find_element(By.XPATH, "//*[text()='Tickets']").click()
    browser.implicitly_wait(30)
    search = browser.find_element(By.NAME,"query")
    search.send_keys("21000" + Keys.RETURN)
    browser.implicitly_wait(30)
    browser.find_element(By.LINK_TEXT,"21000").click()
    browser.implicitly_wait(30)
    assert "Cake" in browser.title
    browser.quit()


def test_silhouetteamerica_signin():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.set_window_size(1920,1080)
    browser.get('http://www.silhouetteamerica.com/')
    time.sleep(3)  # Let the user actually see something!
    browser.find_element(By.CSS_SELECTOR,'.nav-link > .material-icons-outlined').click()
    browser.quit()


def test_confirm_yahoo_title():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.get('http://www.yahoo.com')
    browser.implicitly_wait(30)
    browser.find_element(By.NAME,"agree").click()
    browser.implicitly_wait(30)
    assert 'Yahoo' in browser.title

    elem = browser.find_element(By.NAME, 'p')  # Find the search box
    elem.send_keys('Silhouette America' + Keys.RETURN)
    browser.quit()