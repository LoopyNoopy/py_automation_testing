import subprocess
import pytest
import os

@pytest.fixture(scope="session",autouse=True)
def install_requirements():
    print("Assigning GitHub token")
    os.environ['GH_TOKEN'] = "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"
    my_value = os.environ.get('GH_TOKEN')
    if my_value:
        print(f"The value of GH_TOKEN is: {my_value}")
    else:
        print("GH_TOKEN is not set.")
    os.environ['NODE_OPTIONS'] = '--tls-min-v1.2'
    my_value = os.environ.get('NODE_OPTIONS')
    if my_value:
        print(f"The value of NODE_OPTIONS is: {my_value}")
    else:
        print("NODE_OPTIONS is not set.")

    print("Instaling Node, Puppeteer for Chrome and Firefox")
    install_puppeteer_commands = [
        "winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements",
        "winget install -e --id Opera.Opera",
        "npm config set registry https://registry.npmjs.org/",
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