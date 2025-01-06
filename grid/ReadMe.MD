Selenium Grid Documentation
===========
```
@/*****************************************************************************(
@******************************************************************************/
@******************************************************************************/
@***************************************************************@@@@@@/********/
@************************************************************/@@@@@@@@@@/******/
@******************************************************&@@@@@@@@@@@@@@@@@******/
@*****************************************************@@@****/@@@@@@@@@@/******/
@******************************************((/*******/@@#*******&@@@@@/********/
@**************************************#@@@@@@@@@****/@@#**********************/
@*************************************#@@@@@@@@@@@@@@@@@#**********************/
@*************************************/@@@@@@@@@@@***/@@#**********************/
@***************************************@@@@@@@@#****/@@#**********************/
@****************************************************/@@#******@@@@@@@@********/
@*****************************************************@@@#***#@@@@@@@@@@&******/
@*******************************************************@@@@@@@@@@@@@@@@@******/
@*************************************************************@@@@@@@@@@*******/
@*************#@@@@@@@@@@@@@@@@(*********************************#&&%/*********/
@**********(@@@@@@@@@@@@@@@@@@@@@@@/*******************************************/
@*********@@@@@@@@@(****/%@@@@@@@@*********************************************/
@********%@@@@@@@*************(@(***************#@@@@@@@@%/********************/
@********#@@@@@@@@(*************************&@@@@@@@@@@@@@@@@&*****************/
@*********&@@@@@@@@@@@@@@@&***************@@@@@@@@&****#@@@@@@@@***************/
@***********@@@@@@@@@@@@@@@@@@@@&*******/@@@@@@@**********#@@@@@@**************/
@**************/#@@@@@@@@@@@@@@@@@@/****@@@@@@@////////////@@@@@@%*************/
@***********************/#@@@@@@@@@@/***@@@@@@@@@@@@@@@@@@@@@@@@@@*************/
@***********/****************@@@@@@@%***@@@@@@@//////////////////**************/
@*********%@@@@&************#@@@@@@@/***/@@@@@@@/******************************/
@*******/@@@@@@@@@@@@@@@@@@@@@@@@@@/******@@@@@@@@@(****/#@@@@#****************/
@*********/@@@@@@@@@@@@@@@@@@@@@@(**********@@@@@@@@@@@@@@@@@@@&***************/
@***************%@@@@@@@@@@@&/******************%@@@@@@@@@&(*******************/
@******************************************************************************/
@******************************************************************************/
@******************************************************************************/
``` 

# Brief

Our testing system is using Selenium and Appium to control either the Browser or Mobile device respectively.
Because we are using these frameworks, we are able to take advantage of another product from Selenium called the Selenium Grid.
The grid allows us to have multiple nodes with different capability sets as examples:

- Node 1 = Windows 11 with Chrome, Firefox, Internet Explorer, Edge 
- Node 2 = macOS with Chrome, Firefox, Edge and Safari
- Node 3 = Windows 10 with Chrome, and an Android 14 Virtual Device

This system is able to take the capabilities of each test we write (based on the driver setup) and runs and queues them respectively.

# Grid setup

The main server can be run on any machine in the office, but at the time of writing it is running on a semi-dedicated Linux machine along with the RabbitMQ server.
At the time of writing due to how the office network is set up, you need to be connected to the network via a LAN
connection in order to use the Grid

## Requirements 

In order to run either the nodes or the grid yourself need too:

1. Install a JDK from: https://www.oracle.com/java/technologies/downloads/ (Latest is always recommended)
2. Get the .jar file for the Selenium Grid at: https://github.com/SeleniumHQ/selenium/releases
    - The one that Mekhane is using will be in `suite\Testing\Smoke\grid\grid_releases`
3. Once installed, add an environment variable for `JAVA_HOME` - The value of this is the Java installation folder
    - On windows
        1. Start -> Type "Environment variables" - Should come up with `Edit the System Envrioment Variables` - Go in
           there
        2. Click `Environment Variables`
        3. Click the `New` under the `System Variables` section
        4. Set `Variable Name` to `JAVA_HOME`
        5. Set `Variable Value` to... whatever folder is in `C:\Program Files\Java`
            - Example: `C:\Program Files\Java\jdk-20`

# Setting up the grid

Selenium Grid has 3 modes you can use:

- Standalone - Combines Hub and Node for 1 machines **Cannot be connected to a hub**
- Hub - A server to distribute different capability sets to nodes
- Node - A client for the Grid which houses different capability sets.

## Arguments

The selenium grid has a few arguments you can use while setting it up - below are the ones which are used within SRT

| Argument                    | Value                                   | Description                                                                                                                                            |
|-----------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--reject-unsupported-caps` | true                                    | If the Grid gets capabilities it doesn't support instantly reject the test.                                                                            | 
| `--selenium-manager`        | true                                    | Will automatically detect what web browsers can run on the system, and will download the browsers and drivered required during the running of the test |
| `--hub`                     | http://Mekhane.local:4444/grid/register | Used exclusively by nodes so it can connect to the hub                                                                                                 |
| `node`                      | node                                    | Specifies its being run in node mode                                                                                                                   |
| `hub`                       | hub                                     | Specifies its being run in hub mode                                                                                                                    |
| `standalone`                | standalone                              | Specifies its being run in standalone mode                                                                                                             |
| `--config`                  | filepath                                | Allows the use of a configuration file (Used to setup the relay to an Appium server                                                                    |

### Example

```commandline
java -jar "suite\Testing\Smoke\grid\grid_releases\selenium-server-4.21.0.jar" standalone --reject-unsupported-caps true --selenium-manager true --config "D:\Repo\suite\Testing\Smoke\grid\node_config\local_appium_node.toml"
```

## Standalone

If you want to run the Grid standalone you essentially use the following command:

```commandline
java -jar "suite\Testing\Smoke\grid\grid_releases\selenium-server-4.21.0.jar" standalone --reject-unsupported-caps true --selenium-manager true
```

Just remember to change the file path to the .jar file for the absolute path.

To confirm its running, on the same PC that its running enter the following into a browser: http://localhost:4444/ui/
You should see the Grid UI with an active node of what your PC is capable of.

- Just a note that the URL is very sensitive - if you forget the `/` at the end it will appear blank

Also note that the command above will **only** show browser capabilities - for mobile devices you will need to add a
config file to relay to an Appium server which we will go through later in the document.

## Hub (Used on Mekhane)

Hub mode allows you to connect nodes which can have different capability sets dependent on the device that they are
running (I.e: Windows 11, macOS 14, Linux etc)
Using a Grid Hub means that in the test suite, we only need to connect to one machine that will distribute our tests
across all the nodes instead of connecting to each one individually.

Whilst you can use this section as a bases to set up your own hub - this section will be tailored for the current Hub
running on Mekhane.

1. Open a console window
2. Run the following command
   ```commandline
   sudo java -jar 'PycharmProjects/suite/Testing/Smoke/grid/grid_releases/selenium-server-4.21.0.jar' hub --reject-unsupported-caps true
   ```

   Command rundown

   - `sudo` = Run this command as admin
   - `java -jar path/to.jar` = Run this java file - In our case the Grid Java file
   - `hub` = Specify that the Grid is to run in "Hub" mode
   - `--reject-unsupported-caps true` = If the hub gets a capability request that none of the nodes have, reject the request

     - This was done as if not, when you got the capability wrong the test would get stuck in the queue for a bit

3. If done correctly, you should be able to go too: `mekhane.local:4444/ui` and see that the Grid is running

    - At the time of writing, there is a server currently running at: `mekhane.local:4444/ui`

## Node

This section is assuming you are attempting to connect a Node to the current Hub running on Mekhane

Nodes need to be connected to a hub, the command is very similar to starting Grid in Standalone mode. The biggest
difference is using the `--hub` argument to specify the IP / Hostname of the grid you want to connect too.

```commandline
java -jar "C:\Grid Node\selenium-server-4.21.0.jar" node --hub http://mekhane.local:4444/grid/register --selenium-manager true
```

# Set up the Appium server on a node

This is an optional step you can do before setting up the Selenium node **if** you want the node to show the Hub it has mobile device capability
If you do want mobile devices on the node

## Requirements

### Installing the Appium server

1. Install Node.js: https://nodejs.org/en
2. Once installed, set the Environment variable for JAVA_HOME - this should already be set up with installing the GRID
   or Allure

    #### Windows
   1. Start -> Type "Environment variables" - Should come up with `Edit the System Envrioment Variables` - Go in there
   2. Click `Environment Variables`
   3. Click the `New` under the `System Variables` section
   4. Set `Variable Name` to `JAVA_HOME`
   5. Set `Variable Value` to... whatever folder is in `C:\Program Files\Java`
      - Example: `C:\Program Files\Java\jdk-20`
3. Open the terminal and run the command: `npm install --global appium`
4. Once done, restart the terminal and then enter one of the following depending on your mobile device type:

| Device type | Command                                                  | 
|-------------|----------------------------------------------------------|
| Android     | appium driver install uiautomator2                       | 
| iOS         | appium driver install xcuitest                           |
| Windows     | appium driver install --source=npm appium-windows-driver |

* Need to confirm the windows one

Once done, you should be able to go into a terminal window and type `appium` for the appium server to start.

##### Important note

The **BIGGEST** thing you need to make sure works is when you run the appium server, it goes to port `4723` - If it doesn't... **MAKE IT NO MATTER WHAT**.

Basically, it becomes an absolute nightmare to deal with an Appium server if the port is not 4723, as you then need to know about 3 - 4 other ports you then have to pass to the Selenium Node. Keep it simple, keep it 4723, this should never be a problem as Appium defaults to this port when you start it UNLESS you have an Appium server already running. But if another process takes this port kill it and give it to Appium. Also at the time of writing our tests do not support custom Appium ports (Or at least the grid doesn't)

### Setting up an Android device

1. Install [Android Studio](https://developer.android.com/studio?gad_source=1&gclid=Cj0KCQjw9vqyBhCKARIsAIIcLME85gOn2Ag5W81cm8REShV-2Z6hrufcifj6INR88orEEMpMHEWbs6IaAkPvEALw_wcB&gclsrc=aw.ds)
2. Run Android Studio, and close the "First time setup" dialogues until you see `Welcome to Android Studio`
3. One this page you should see `More Actions`
4. If you click it, you should see `SDK Manager...` click that
5. If not installed already, it should take you to a page where most of it is greyed out apart from a blue `edit`
   button. Click on that and go through the installation process
6. Once complete the page should now be enabled, go to the `SDK Tools` tab and make sure the following have a tick.
   If any either have a grey box or a line - that means it is not installed or there is an update, click on the grey box
   or white line to add it to the installer queue.
    - `Android SDK Build-Tools` - This will have a random number and a `rc` number in the name
    - `Android SDK Command-line Tools (latest)`
    - `Android Emulator`
    - `Android Emulator hypervisor driver (installer)` - This might need virtualization enabled in the BIOS before this
      will install
    - `Android SDK Platform-Tools`
7. Once you have made your selection click `Apply` - This will start the installation process.
8. Once installed, add an environment variable for `ANDROID_HOME` - The value of this is Android SDK Location which you
   edited in step 5
    - On windows
        1. Start -> Type "Environment variables" - Should come up with `Edit the System Envrioment Variables` - Go in
           there
        2. Click `Environment Variables`
        3. Click the `New` under the `System Variables` section
        4. Set `Variable Name` to `ANDROID_HOME`
        5. Set `Variable Value` to the SDK folder: `C:\Users\%USERNAME%\AppData\Local\Android\Sdk`
            - Example: `C:\Users\danie\AppData\Local\Android\Sdk`

From this point you can either:

- Set up an Android Emulated device by closing the settings menu, going back
  into `More Actions` -> `Virtual Device Manager`
    - In step 6 it states that the hypervisor driver _might_ need virtualization to be enabled - you need to do this
      through the BIOS, because the BIOS is different dependent on the Motherboard manufacturer I cannot give you
      precise steps on how to enable, what I can give is the following tips:
        - It will more than likely be in the "Advanced" section if there is one
        - It will be under CPU
        - When in windows, you can verify if its enabled by pressing `Ctrl` + `Shift` + `Esc` to open task manager ->
          Click on the `Perfomance` tab and select `CPU` -> You should see `Virtualisation:` to confirm if its enabled
- Enable `Developer Options` on your Android device and connect it via a USB cable

Because of how varied these steps can be based on the phone or the type of device you want to emulate I'm not providing
steps.

What you need to do after you have plugged in your phone / set up your Android device is to do the following:

1. Open Terminal
2. Run `adb devices`

This will check to see if the daemon is running, and list all connected devices. Depending on how many you have made you
should see something like:

```commandline
List of devices attached
M4AIB763B4805UP device
```

Example is me connecting my Asus ZenFone 8 Flip to my PC

## Attaching Appium to a Selenium Grid Node

### 1. Configuring the Selenium node TOML file

In order for the Node to tell the Hub that it can take tests for mobile devices, you need to set up a config file that basically:

- Tells the node what port it is going to be on
- Tell it is going to act as a relay for the appium server running on the same machine

Below is an example of what the toml file for the node config looks like - This example can be found
at `D:\Repo\suite\Testing\Smoke\grid\node_config\local_appium_node.toml`

```toml
[server]
port = 9999

[relay]
url = "http://127.0.0.1:4723"
status-endpoint = "/status"
configs = [
    "1", "{\"platformName\": \"android\", \"appium:platformVersion\": \"11\", \"appium:automationName\": \"UIAutomator2\"}",
    "1", "{\"platformName\": \"android\", \"appium:platformVersion\": \"13\", \"appium:automationName\": \"UIAutomator2\"}"
]
```

#### toml rundown

```toml
[server]
port = 9999
```

Tells the server what port to use - make sure that the port you put here is free on your system
Once Ticket 110 is complete it will give itself a free port

```toml
[relay]
url = "http://127.0.0.1:4723"
status-endpoint = "/status"
```

Relay of the Appium node - the ip will be the IP address of the system you want the node to run on. The port number is the one Appium is listening too.

```toml
configs = [
    "1", "{\"platformName\": \"android\", \"appium:platformVersion\": \"11.0\", \"appium:automationName\": \"uiautomator2\"}",
    "1", "{\"platformName\": \"android\", \"appium:platformVersion\": \"8.1\", \"appium:automationName\": \"uiautomator2\"}"
]
```

This is telling the Grid what mobile devices it can connect to on this node.

- `"1"` - is the amount of sessions that can be run at a time with this set.
  - So if you have say 2 Android 11 Virtual devices, you can set the "1" to a "2"
- The rest of the line is basically JSON of the capabilities of the device - these can be whatever as long as they match up to the capabilities listed at: https://appium.io/docs/en/2.2/guides/caps/
  - The basic format of this though is:
    - `\"cap\":\"value\"`
  - The bare minimum you need is:
    - `\"platformName\": \"value\"` = Android / iOS etc - look at https://appium.io/docs/en/2.0/ecosystem/
    - `\"appium:platformVersion\": \"value\"` = Version num of the os
    - `\"appium:automationName\": \"uiautomator2\"` = Automation driver - gotta match the installation key at: https://appium.io/docs/en/2.0/ecosystem/ for the platform specified at platform name

What you need to do is firstly edit the configs, so they match the capability of the device connected to your PC be it
either an Emulated device or a Physical one

If you are using the `local_appium_node.toml` all you need to do is modify the platform version to be the same as it
shows on your device.

### 2. Start the Appium server

In the repo you will find: `suite\Testing\Smoke\grid\appium_config\appium.yml`

All this does is specify port 4723 and that it is using the UiAutomator 2 driver for Android

In a command line, run the following - make sure to put the absolute path in for the .yml file

```commandline
appium --config D:\Repo\suite\Testing\Smoke\grid\appium_config\appium.yml
``` 

### 3. Start Selenium with the Appium relay

1. Open another Terminal window / Tab

2. Write the command for either starting a Selenium in Node or Standalone mode as shown higher up in the readme file *
   *but** add the `--config` command to then specify the TOML file you have made like so:

    Standalone
    
    ```commandline
    java -jar "C:\Users\dburgess\PycharmProjects\suite\Testing\Smoke\grid\grid_releases\selenium-server-4.21.0.jar" standalone --reject-unsupported-caps true --selenium-manager true --config "D:\Repo\suite\Testing\Smoke\grid\node_config\local_appium_node.toml"
    ```
    
    Node
    
    ```commandline
    java -jar "C:\Users\dburgess\PycharmProjects\suite\Testing\Smoke\grid\grid_releases\selenium-server-4.21.0.jar" node --config "C:\Users\dburgess\PycharmProjects\suite\Testing\Smoke\grid\node_config\local_appium_node.toml" --hub http://Mekhane.local:4444/grid/register --selenium-manager true
    ``` 

3. Check the "UI link" of your Grid hub your node should appear with all the browsers your device can do and any Android
   devices configured in the TOML

# Troubleshooting

## Cannot register with Hub

There have been a couple of times when the nodes could not register with the Hub. What I have found is this is due to
either Appium or Selenium defaulting to a network adapter which is not the ethernet.

At this point in time if you run into this issue - the way I have resolved this is by either disabling the network
adapter in `Control Panel` -> `Network and Internet` -> `Network Connections`

If disabling doesn't work, you need to uninstall the service which has provided the adapter - Usual culprits are:

- VPN clients like Open VPN
- Virtual Machine software like Virtual Box or Hyper-V
- WAN services like LogMeIn Hamachi