import pytest
import os
import subprocess
import requests
import tqdm

def add_to_path(path):
    current_path = os.environ.get("PATH", "")
    new_path = f"{current_path}{os.pathsep}{path}"
    os.environ["PATH"] = new_path

@pytest.fixture(scope="session",autouse=True)
def install_requirements():
    install_commands = [
        "winget install OpenJS.NodeJS.LTS --accept-package-agreements --accept-source-agreements",
        "winget install -e --id Oracle.JDK.19 --accept-package-agreements --accept-source-agreements",
        "winget install -e --id Google.AndroidStudio --accept-package-agreements --accept-source-agreements",
        "npm i -g appium@next",
        "appium driver install uiautomator2"]
    for command in install_commands:
        os.system(command)

    add_to_path("C:\Users\\" + os.getlogin() + "\\AppData\Local\Android\Sdk\platform-tools")
    add_to_path("C:\Users\\" + os.getlogin() + "\\AppData\Local\Android\Sdk\cmdline-tools\latest\bin")
    add_to_path("C:\Users\\" + os.getlogin() + "\\AppData\Local\Android\Sdk\emulator")

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

    # Start appium in another terminal window, so we can still use the python script
    subprocess.run(["start", "cmd", "/k", "appium"], shell=True)

def find_java_version():
    items = os.listdir("C:\\Program Files\\Java\\")
    return items[0]

import subprocess

# Define AVD parameters
avd_name = "pixel_5"
avd_target = "android-34"  # e.g., "android-30"
avd_abi = "x86_64"  # e.g., "x86_64" or "armeabi-v7a"

# Create the AVD
create_avd_command = f"avdmanager create avd -n {avd_name} -k '{avd_target}' --abi {avd_abi}"
subprocess.run(create_avd_command, shell=True, check=True)
