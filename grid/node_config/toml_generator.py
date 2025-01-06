import subprocess
import re
import toml


# Requires Selenium Manager to be downloaded:
# https://github.com/SeleniumHQ/selenium/blob/trunk/common/selenium_manager.bzl
# https://www.selenium.dev/documentation/selenium_manager/

def get_paths(browser, version):
    command = [
        "C:\\Users\\dburgess\\Downloads\\selenium-manager-windows.exe",
        "--browser", browser,
        "--browser-version", version
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print(f"Error running Selenium Manager: {result.stderr}")
        return None, None

    output = result.stdout
    print("Command output:\n", output)

    driver_path_pattern = re.compile(r"Driver path:\s*(.*)")
    browser_path_pattern = re.compile(r"Browser path:\s*(.*)")

    driver_path_match = driver_path_pattern.search(output)
    browser_path_match = browser_path_pattern.search(output)

    driver_path = driver_path_match.group(1) if driver_path_match else None
    browser_path = browser_path_match.group(1) if browser_path_match else None

    return driver_path, browser_path


def write_to_toml(driver_configurations):
    toml_data = {
        'node': {
            'driver-configuration': driver_configurations,
            'nodeTimeout': 120,
            'maxSession': 10
        }
    }

    with open('selenium_config.toml', 'w') as toml_file:
        toml.dump(toml_data, toml_file)


def generate_stereotype(browser, version):
    stereotype = {
        "browserName": browser,
        "browserVersion": version,
    }
    return stereotype


# Example usage
browser = "chrome"
versions = ["stable", "beta", "dev", "canary"]

driver_configurations = []

for version in versions:
    driver_path, _ = get_paths(browser, version)
    if driver_path:
        stereotype = generate_stereotype(browser, version)
        display_name = f"{browser.capitalize()} {version.capitalize()}"
        config_string = f'display-name="{display_name}" max-sessions=5 webdriver-path="{driver_path}" stereotype="{toml.dumps(stereotype).strip()}"'
        driver_configurations.append(config_string)
    else:
        print(f"Failed to retrieve paths for {browser} {version}.")

write_to_toml(driver_configurations)
