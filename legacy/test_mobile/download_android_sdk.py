from tqdm import tqdm
import zipfile
import subprocess
import requests
import os

def download_android_sdk() -> None:
    # Define the URL to download the Android SDK tools
    sdk_download_url = "https://dl.google.com/android/repository/commandlinetools-win-6858069_latest.zip"

    # Define the path where you want to save the downloaded SDK tools
    sdk_download_path = "android_sdk\\"

    # Create the output directory if it doesn't exist
    os.makedirs(sdk_download_path, exist_ok=True)

    # Define the file name for the downloaded SDK tools
    sdk_zip_file = os.path.join(sdk_download_path, "sdk-tools.zip")

    # Download the SDK tools
    response = requests.get(sdk_download_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(sdk_zip_file, "wb") as file, tqdm(
        desc="Downloading SDK",
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            bar.update(len(data))

    print("SDK tools downloaded to:", sdk_zip_file)

    # You can add code to extract the downloaded SDK tools if needed
    with zipfile.ZipFile(sdk_zip_file, "r") as zip_ref:
        zip_ref.extractall(sdk_download_path)

    print("SDK tools extracted to:", sdk_download_path)
    return

def start_emulator():

    os.environ['ANDROID_SDK_ROOT'] = os.getcwd() + "\\android_sdk"
    my_value = os.environ.get('ANDROID_SDK_ROOT')
    if my_value:
        print(f"The value of ANDROID_HOME is: {my_value}")
    else:
        print("ANDROID_HOME is not set.")

    avd_create_command = "avdmanager create avd -n MyEmulator -k 'system-images;android-30;google_apis;x86_64' --device 'pixel'"
    emulator_start_command = "emulator -avd MyEmulator"

    # Create the AVD configuration
    subprocess.run(avd_create_command, shell=True, check=True)

    # Start the emulator
    subprocess.run(emulator_start_command, shell=True, check=True)


def download_android_sdk_2():


    # Set the URL for downloading the Android SDK
    android_sdk_url = "https://developer.android.com/studio"

    # Define the directory where you want to save the SDK
    download_dir = os.getcwd() +"\\android_sdk"

    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Set the file name for the downloaded SDK
    sdk_filename = "android_sdk.zip"

    # Download the Android SDK
    response = requests.get(android_sdk_url)
    if response.status_code == 200:
        with open(os.path.join(download_dir, sdk_filename), "wb") as sdk_file:
            sdk_file.write(response.content)
        print(f"Android SDK downloaded to {os.path.join(download_dir, sdk_filename)}")
        with zipfile.ZipFile(download_dir+"\\"+sdk_filename, "r") as zip_ref:
            zip_ref.extractall(download_dir+"\\"+sdk_filename)

        print("SDK tools extracted to:", download_dir+"\\"+sdk_filename)
    else:
        print("Failed to download Android SDK")




current_directory = os.getcwd()

print("Current Working Directory:", current_directory)


def download_android_sdk_3():
    import subprocess

    # Set the URL for downloading the Android SDK
    android_sdk_url = "https://developer.android.com/studio"

    # Define the directory where you want to save the SDK
    download_dir = os.getcwd() +"\\android_sdk"

    os.makedirs(download_dir, exist_ok=True)

    # Set the file name for the downloaded SDK
    sdk_filename = "android_sdk.zip"

    # Use wget to download the Android SDK
    subprocess.run(["wget", android_sdk_url, "-O", os.path.join(download_dir, sdk_filename)])
    print(f"Android SDK downloaded to {os.path.join(download_dir, sdk_filename)}")


def download_sdk_4():
    import requests
    import os

    # Set the direct download URL for the Android SDK command-line tools
    android_sdk_url = "https://dl.google.com/android/repository/commandlinetools-{platform}-7302050_latest.zip"

    # Define the directory where you want to save the SDK
    download_dir = os.getcwd() +"\\android_sdk"

    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Set the file name for the downloaded SDK
    sdk_filename = "android_sdk.zip"

    # Determine the appropriate platform for your system (e.g., windows, mac, linux)
    # Replace 'your_platform' with the correct platform name
    your_platform = "windows"

    # Substitute the platform name into the URL
    android_sdk_url = android_sdk_url.format(platform=your_platform)

    # Download the Android SDK
    response = requests.get(android_sdk_url)
    if response.status_code == 200:
        with open(os.path.join(download_dir, sdk_filename), "wb") as sdk_file:
            sdk_file.write(response.content)
        print(f"Android SDK downloaded to {os.path.join(download_dir, sdk_filename)}")
    else:
        print("Failed to download Android SDK")


#download_sdk_4()

def latest_version_finder():
    import requests
    from bs4 import BeautifulSoup

    # URL of the Android Command Line Tools download page
    url = "https://developer.android.com/studio#command-tools"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element containing the latest version information
        version_element = soup.find("a", {"class": "button dark download"})

        # Extract the version from the element
        latest_version = version_element.get("data-version")

        print(f"The latest version of Android SDK is: {latest_version}")
    else:
        print("Failed to fetch the Android SDK page")

download_android_sdk()

add_to_path("C:\Users\\"+os.getlogin()+"\\AppData\Local\Android\Sdk\platform-tools")
add_to_path("C:\Users\\"+os.getlogin()+"\\AppData\Local\Android\Sdk\cmdline-tools\latest\bin")
add_to_path("C:\Users\\"+os.getlogin()+"\\AppData\Local\Android\Sdk\emulator")