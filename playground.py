import os
import subprocess
import asyncio
import subprocess
from appium import webdriver
import pyuac

def find_java_version():
    items = os.listdir("C:\\Program Files\\Java\\")
    return items[0]

def install_appium():
    install_commands = [
    "winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements",
    "winget install -e --id Oracle.JDK.19 --accept-package-agreements --accept-source-agreements",
    "winget install -e --id Google.AndroidStudio --accept-package-agreements --accept-source-agreements",
    "npm i -g appium@next",
    "appium driver install uiautomator2"]
    for command in install_commands:
        os.system(command)

    subprocess.run(["start", "cmd", "/k", "appium"], shell=True)

    #Set envrioment variable for JDK version installed
    os.environ['JAVA_HOME'] = 'C:\\Program Files\\Java\\' + find_java_version()
    my_value = os.environ.get('JAVA_HOME')
    if my_value:
        print(f"The value of JAVA_HOME is: {my_value}")
    else:
        print("JAVA_HOME is not set.")

    os.environ['ANDROID_HOME'] = "C:\\Users\\"+os.getenv("USERNAME")+"\\AppData\\Local\\Android\\Sdk"
    my_value = os.environ.get('ANDROID_HOME')
    if my_value:
        print(f"The value of ANDROID_HOME is: {my_value}")
    else:
        print("ANDROID_HOME is not set.")



current_directory = os.getcwd()

print("Current Working Directory:", current_directory)

def install_android():

    from pywinauto import application
    import time

    # Start the application (replace 'notepad.exe' with the target application)
    app = application.Application(backend="uia").start('C:\Program Files\Android\Android Studio\\bin\studio64.exe', wait_for_idle=True)

    # Print control identifiers to the console
    time.sleep(5)
    child_window = app.window(title="Android Studio Setup Wizard")
    child_window.dump_tree()

    import keyboard

    # Simulate a keypress
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('right')
    time.sleep(0.5)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')



    # Optional: Add a delay to observe the output (in seconds)
    import time

    # Close the application
    #app.kill()


    from selenium import webdriver
    from webdriver_manager.firefox import GeckoDriverManager


def add_to_path(path):
    current_path = os.environ.get("PATH", "")
    new_path = f"{current_path}{os.pathsep}{path}"
    os.environ["PATH"] = new_path

add_to_path("C:\\Users\\" + os.getlogin() + "\\AppData\Local\Android\Sdk\platform-tools")
add_to_path("C:\\Users\\" + os.getlogin() + "\\AppData\Local\Android\Sdk\cmdline-tools\latest\bin")
add_to_path("C:\\Users\\" + os.getlogin() + "\\AppData\Local\Android\Sdk\emulator")

# Set envrioment variable for JDK version installed
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

#ToDo - restart the terminal or make these commands work in a new one
#ToDo - make this dynamic to the latest version THEN download version based on appium caps
os.system('sdkmanager "platforms;android-34"')
os.system('sdkmanager "system-images;android-34;google_apis;x86_64"')