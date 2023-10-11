import subprocess

import os


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
        "winget install -e --id Oracle.JDK.19 --accept-package-agreements --accept-source-agreements",
        "winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements",
        "winget install -e --id Opera.Opera",
        "winget install -e --id Google.AndroidStudio --accept-package-agreements --accept-source-agreements",
        "npm i -g appium@next",
        "appium driver install uiautomator2"
        "npm config set registry https://registry.npmjs.org/",
        "npm install --global npm",
        "npm install -g npx",
        "npm i allure-commandline",
        "npm i puppeteer",
        "npm i @puppeteer/browsers",
        "npx @puppeteer/browsers install firefox",
        "npx @puppeteer/browsers install chrome",
        "npx @puppeteer/browsers install chromedriver",
        "pip install --upgrade pytest pytest-allure-adaptor allure-pytest"]
    for command in install_puppeteer_commands:
        os.system(command)


os.environ['JAVA_HOME'] = 'C:\\Program Files\\Java\\' + find_java_version()
my_value = os.environ.get('JAVA_HOME')
if my_value:
    print(f"The value of JAVA_HOME is: {my_value}")
else:
    print("JAVA_HOME is not set.")

os.environ['ANDROID_HOME'] = "C:\\Users\\" + os.getenv("USERNAME") + "\\AppData\\Local\\Android\\Sdk"
my_value = os.environ.get('ANDROID_HOME')
if my_value:
    print(f"The value of ANDROID_HOME is: {my_value}")
else:
    print("ANDROID_HOME is not set.")


install_requirements()