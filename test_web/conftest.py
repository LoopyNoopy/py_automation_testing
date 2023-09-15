import pytest
import os


@pytest.fixture(scope="session",autouse=True)
def browser_install():
    os.environ['GH_TOKEN'] = "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"
    install_puppeteer_commands = [
        "winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements",
        "winget install -e --id Opera.Opera",
        "npm install --global npm",
        "npm install -g npx",
        "npm i puppeteer",
        "npm i @puppeteer/browsers",
        "npx @puppeteer/browsers install firefox",
        "npx @puppeteer/browsers install chrome",
        "npx @puppeteer/browsers install chromedriver"]
    for command in install_puppeteer_commands:
        os.system(command)
    yield


@pytest.fixture()
def get_chrome_version_folder():
    items = os.listdir("chrome")
    return items[0]


@pytest.fixture()
def get_firefox_version_folder():
    items = os.listdir("firefox")
    return items[0]


@pytest.fixture()
def get_chromedriver_version_folder():
    items = os.listdir("chromedriver")
    return items[0]

@pytest.fixture()
def get_chicken_nugget():
    print("chicken")
    return