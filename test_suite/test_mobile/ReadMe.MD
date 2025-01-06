Setting up Appium for development of Silhouette Go tests
===========

```
                                      (((                                       
                          ((((((((((((((((((((((((((((                          
                    (((((((((((((((((((((((((((((((((((((((                     
                /(((((((((((((((((((((((((((((((((((((%%%%%%%%(                 
             ((((((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%              
           (((((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%           
         ((((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         
       ((((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%       
     /((((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     
    (((((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#   
   (((((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
  (((((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
  ((((((((((((((((((((((((((((((((    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
 (((((((((((((((((((((((((((((((((         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 ((((((((((((((((((((((((((((((((             ,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 .(((((((((((((((((((((((((((((((                 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
...((((((((((((((((((((((((((((((                   %%%%%%%%%%%%%%%%%%%%%%%%%%%%
 ...,((((((((((((((((((((((((((((                  ....%%%%%%%%%%%%%%%%%%%%%%%%%
 ......((((((((((((((((((((((((((              ..........%%%%%%%%%%%%%%%%%%%%%%%
 ........*(((((((((((((((((((((((        ..................%%%%%%%%%%%%%%%%%%%%%
  ............((((((((((((((((((( ..........................%%%%%%%%%%%%%%%%%%% 
  ...........................................................%%%%%%%%%%%%%%%%%  
   ...........................................................%%%%%%%%%%%%%%%   
    ..........................................................%%%%%%%%%%%%%%    
     ..........................................................%%%%%%%%%%%%     
       .......................................................%%%%%%%%%%%       
         .....................................................%%%%%%%%%         
           ..................................................%%%%%%%%           
             ...............................................%%%%%%              
                ...........................................%%%%                 
                    .....................................%                      
                         ...........................                            
```

# Brief

Appium is using to control the mobile devices which we run our automated tests for Silhouette Go
This guide will go through the steps to set up your PC, so you can start writing tests using the Appium framework for Android and iOS devices

It is recommended to use a combination of Windows and Android to develop the tests for Silhouette Go, it is possible to create tests using macOS and iOS, but it is easier to set up the tests with Window and Android.
This guide will assume you are using Windows and Android.

# Initial setup

## Requirements

1. Java JDK - https://www.oracle.com/middleeast/java/technologies/downloads/
2. NodeJS - https://nodejs.org/en/download/prebuilt-installer
3. Appium **JAVA JDK and Node.js is required before installing** - https://appium.io/docs/en/2.2/quickstart/install/
4. Android Studio - https://developer.android.com/studio
5. Appium Inspector - https://github.com/appium/appium-inspector/releases
6. Appium Device Drivers - https://appium.io/docs/en/2.3/ecosystem/drivers/

## Installing the Java JDK - Java Development Kit

1. Go to: https://www.oracle.com/middleeast/java/technologies/downloads/
2. Select your platform and download the installer **Not the MSI Installer**
3. Run the installer
4. Press the Start button and type in `env` -> This should show `Edit the System Environment Variables`, click on that.
5. Click on `Enviroment Variables` near the bottom right
6. Under `System Variables` click on `New`
7. Make the `Variable name` -> `JAVA_HOME`
8. Open a file explorer window
9. Go to: `C:\Program Files\OpenJDK` and you should see a folder inside like: `jdk-22.0.2`
10. You want to make the `Variable Value` the full file path of the JDK version you have like so:
    - `C:\Program Files\OpenJDK\jdk-22.0.2`
11. Done! :D

## Node JS

This requires the Java JDK to be installed

1. Go too https://nodejs.org/en/download/prebuilt-installer and download the installer for your system
2. Run through the installer
3. Done! :D

## Appium

This requires Node.js to be installed

1. Open a command prompt window
2. Run `npm i --location=global appium`
3. Done! :D

## Android Studio

1. Download Android Studio at https://developer.android.com/studio
2. Run the installer
3. Open Android Studio
4. When it first runs, it might ask you the type of app you are going to create, click cancel on this screen
5. This will then leave a window called `Welcome to Android Studio`
6. On this screen click on `More Actions` and then `SDK Manager`
7. At the top there will be a `Android SDK Location` box which might be empty, if it is -> click on `Edit` and go through the install process
8. Afterward all the options will now be available underneath, click on `SDK Tools`
9. Check `Android SDK Command-line Tools` and click apply
   - There is a change that it is already installed and has a `-` instead of a check - this means there is an update available
10. Let the installation process complete
11. Press the Start button and type in `env` -> This should show `Edit the System Environment Variables`, click on that.
12. Click on `Enviroment Variables` near the bottom right
13. Under `System Variables` click on `New`
14. Make the `Variable name` -> `ANDROID_HOME`
15. Open a file explorer window
16. Go to: `C:\Users\%USERNAME%\AppData\Local\Android\Sdk` and you should see a folder called `platform-tools`
17. You want to make the `Variable Value` the file path to the Android SDK folder like so:
    - `C:\Users\dburgess\AppData\Local\Android\Sdk`
      - **Do not copy and paste from the ReadMe, you need to add your username folder instead of mine**
18. Click `Ok` and find the `Path` entry under `System Variables`
19. Double click it
20. CLick on new
21. Enter the file path above, but add `platform-tools` like so:
    - `C:\Users\dburgess\AppData\Local\Android\Sdk\platform-tools`
      - **Do not copy and paste from the ReadMe, you need to add your username folder instead of mine**
22. Done! :D

## Appium inspector

This tool allows you to connect to the mobile device running on your Appium server to find out how to select the elements that are on screen

1. Go to https://github.com/appium/appium-inspector/releases
2. Download from the `Assets` section
   - You might have to click `Show all assets` to find the Windows version
   - Should end in `win-x64.exe`
3. Run the installer -> Windows will give you a warning, run anyway
4. Done! :D

## Appium drivers

For Appium to control the devices you need to install the appropriate driver. 

1. Open command line
2. Run the following command
3. `appium driver install <installation key>`

Use the table below for the installation keys, this table is a list of all the Official Appium drivers
For basic tests, you will need the UIAutomator2 driver for android, so the command will be the following:

`appium driver install uiautomator2`

| Driver       | Installation Key | Platform(s)                    | Mode(s)             |
|--------------|------------------|--------------------------------|---------------------|
| Chromium     | chromium         | macOS, Windows, Linux          | Web                 |
| Espresso     | espresso         | Android                        | Native              |
| Gecko        | gecko            | macOS, Windows, Linux, Android | Web                 |
| Mac2         | mac2             | macOS                          | Native              |
| Safari       | safari           | macOS, iOS                     | Web                 |
| UiAutomator2 | uiautomator2     | Android                        | Native, Hybrid, Web |
| XCUITest     | xcuitest         | iOS                            | Native, Hybrid, Web |

# Creating tests for Silhouette Go using the Appium Inspector

In order to create tests for Silhouette Go, you need to know how what elements to click / drag / type in.
For this we use a tool called the Appium Inspector, which allows us to connect to a device to see any details about an element we may need.

To start using this you need the following:
1. The Appium server running
2. An Android device connected to the PC the Appium server is hosted on
3. Appium inspector

## Starting the Appium server

Luckily this part is quite easy:

1. Open the command line
2. Type `appium`
3. Hit enter

This will start the Appium service - please note a prompt for Node.JS might appear, allow it.

If you have followed the steps your Appium server will be able to take over and Android device that it can detect.

## Setting up an Android device

You can use either a physical Android device or a virtual device

### Physical Device

1. Before doing anything, you need to enable USB Debugging on the device by doing the following:
   1. Go to settings
   2. Find the details about the device you're using, you're looking for the following:
      - Android version
      - Kernel Version
      - Build number
   3. Spam tap these numbers until developer mode gets enabled
   4. Open `Developer Options` -> This might be on the main settings menu or in System (Each Android device is different)
   5. Scroll down and find `USB debugging` and enable
      - Just a little side note, it might be an idea to also enable `Show taps`
2. Connect the device via USB cable
3. Confirm it's connected by doing the following:
   1. Open Command Window
   2. Type `adb devices`
      - If you're first time running this command, it might ask for permission - click allow
   3. You should see an entry under `list of devices attached`
4. Done! :D

### Virtual Device

1. Open `Android Studio`
2. Click on `More Actions` -> `Virtual Device Manager`
3. Click on `Create Virtual Device`
4. Pick any phone type you like the look of
5. Choose an API Level
   - Try to avoid the Privacy Sandbox versions
   - Try and use one where the target gives an Android version number, not an API level
   - If not installed, click on the little install button in the `Release Name` and install
6. Give it a simple name - I normally go for `DansAVD` and click finish
7. You should now find a Virtual Device in the device manager with a play button to start the AVD

## Using the Appium Inspector

Once you have Appium running and an Android device connected, you can now open the Appium Inspector

When you open the Appium inspector it is going to ask you to enter the Capabilities of the device you want to connect too.
As an absolute minimum, you need the following capabilities to connect to any Android device on your Appium server
   
```json
   {
     "appium:automationName": "uiautomator2",
     "platformName": "Android"
   }
```

You are able to send a lot of different capabilities through Appium either via the inspector or Python script.
Below is a table of globally recognised capabilities:

| Capability                          | Type    | Required? | Description                                                                                                                                                                                                                                   |
|-------------------------------------|---------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| platformName                        | string  | yes       | The type of platform hosting the app or browser                                                                                                                                                                                               |
| appium:automationName               | string  | yes       | The name of the Appium driver to use                                                                                                                                                                                                          |
| browserName                         | string  | no        | The name of the browser to launch and automate, if the driver supports web browsers as a special case                                                                                                                                         |
| appium:app                          | string  | no        | The path to an installable application                                                                                                                                                                                                        |
| appium:appActivity                  | string  | yes       | The Activity to start if you have specified an app to install                                                                                                                                                                                 |
| appium:deviceName                   | string  | no        | The name of a particular device to automate, e.g., iPhone 14 (currently only actually useful for specifying iOS simulators, since in other situations it's typically recommended to use a specific device id via the appium:udid capability). |
| appium:platformVersion              | string  | no        | The version of a platform, e.g., for iOS, 16.0                                                                                                                                                                                                |
| appium:newCommandTimeout            | number  | no        | The number of seconds the Appium server should wait for clients to send commands before deciding that the client has gone away and the session should shut down                                                                               |
| appium:noReset                      | boolean | no        | If true, instruct an Appium driver to avoid its usual reset logic during session start and cleanup (default false)                                                                                                                            |
| appium:fullReset                    | boolean | no        | If true, instruct an Appium driver to augment its usual reset logic with additional steps to ensure maximum environmental reproducibility (default false)                                                                                     |
| appium:eventTimings                 | boolean | no        | If true, instruct an Appium driver to collect Event Timings (default false)                                                                                                                                                                   |
| appium:printPageSourceOnFindFailure | boolean | no        | If true, collect the page source and print it to the Appium log whenever a request to find an element fails (default false)                                                                                                                   |

Ones I would recommend using are:

 - appium:app -> If you give the path to an APK on your machine, it will try and install and launch the app for you
   If you use this capability, you need to also include the appium:appActivity capability which tells Appium in what state to open the app below is an example of adding an app to the capability set

 ```json
   {
      "appium:automationName": "uiautomator2",
      "platformName": "Android",
      "appium:app": "C:\\Users\\dburgess\\Downloads\\com.SilhouetteSoftware.SilhouetteGo.apk",
      "appium:appActivity": "crc64a817c78ca7edff55.SplashActivity"
   }
 ```

 - appium:noReset -> Stops Appium from cleaning up the device when closing a session (Can be useful if you want to leave the device in a certain state)
 - appium:platformVersion -> States the version of the OS you want to use 
 - appium:deviceName -> If you are targeting a specific device on the grid you can give the name of the device

Once you have defined your capabilities you can press the `Start Session` button in the bottom right. This will attempt to connect to your Android device through the Appium server

From this point on, you are able to use the inspector to do the following:

- Find out about any UI element and its attribute
- Tap UI elements / Send keystrokes / Click and Drag on XY co-ordinate
- Send specific commands to the device
- Automatically record a Python script with basic steps 
- Download screenshots of the device
