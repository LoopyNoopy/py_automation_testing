QA Automated tests for test_suite
===========

```
                  //////////////////////////////////////////                    
                   ////////////////////////////////////////(                    
                    ////////  #%%%%%%%  ((((((((  ********                      
                    ////////  #%%%%%%%  ((((((((  ********                      
                    ////////  #%%%%%%%  ((((((((  ********                      
                    ////////  #%%%%%%%  ((((((((  ********                      
                    ////////  #%%%%%%%  ((((((((  ********                      
                    ////////  #%%%%%%%  ((((((((  ********                      
                    ////////  #%%%%%%%  ((((((((                                
                    ////////  #%%%%%%%  ((((((((                                
                    ////////  #%%%%%%%  ((((((((                                
                    ////////  #%%%%%%%                                          
                    ////////  #%%%%%%%                                          
                    ////////  #%%%%%%%                                          
                    ////////  #%%%%%%%                                          
                    ////////                                                    
                    ////////                                                    
                    ////////                                                    
```

## Contents
- [Contents](#Contents)
- [Running the tests](#Running-the-tests)
  - [Brief](#Brief)
  - [PyTest command line](#PyTest-command-line)
    - [Default pytest command](#Default-PyTest-command)
    - [test_suite arguments](#test_suite-arguments)
    - [Other PyTest arguments](#Other-PyTest-Arguments)
      - [X-Dist](#X-Dist)
        - [XDist example use](#XDist-example-use)
      - [Rerun failures](#rerun-failures)
        - [Rerun example use](#Rerun-example-use)
      - [Allure](#Allure)
        - [Viewing the Allure report](#Viewing-the-Allure-report)
  - [PyCharm run configuration](#PyCharm-run-configuration)
- [Writing tests](#Writing-tests)
  - [Allure Decorators](#Allure-decorators)
    - [What is a decorator?](#What-is-a-decorator)
    - [Allure Suite](#Allure-suite)
      - [Suite variables](#Suite-variables)
    - [Allure story](#Allure-story)
      - [Story variables](#Story-variables)
    - [Allure attributes](#Allure-attributes)
    - [Other Allure decorators](#Other-Allure-decorators)
      - [Allure issue](#allure-issue)
      - [Allure link](#Allure-link)
    - [Dynamic Allure attributes](#Dynamic-Allure-attributes)
      - [Allure dynamic title](#Allure-dynamic-title)
      - [Allure dynamic tag](#Allure-dynamic-tag)
    - [Allure steps](#Allure-steps)
      - [Step decorator](#Step-decorator)
      - [With Allure step](#With-Allure-step)
  - [Test Logger](#Test-Logger)
    - [Adding the test_logger to tests](#Adding-the-test_logger-to-tests)
      - [Using the tst logger](#Using-the-test-logger)
      - [Driver Functions](#Driver-Functions)

# Running the tests

## Brief

Our test framework is run through PyTest. The most basic thing you need to know is that pytest will treat any folder,
file and function that starts with `test_` or ends in `_test` as either:

- Folder = Test Suite
- File = Test Module
- Function = Test

In our project, **our standard is to start all of our tests with `test_`**

This means that to run either our tests you need to do the following in the command line:

- Whole suite = `pytest /path/to/test_folder`
- Test Module = `pytest /path/to/test_file.py`
- Single test = `pytest /path/to/test_file.py -k "test_name"`
    - Please note, that the `-k` parameter will tell pytest to run all tests which have that string in the title

## PyTest command line

### Default PyTest command

This command line is an example of the full pytest command you would need to run the tests for test_suite

Please note if you want to copy and paste this example you will need to change:

- The test_suite folder
- Variables for:
    - apk_path
    - web_url

```commandline
pytest C:\path\to\test_suite -n logical --alluredir=allure-results --apk_path C:\Downloads\com.SilhouetteSoftware.SilhouetteGo.apk --web_url https://victorious-pond-024db0f10-preview.centralus.4.azurestaticapps.net/ 
```

Below is an explanation of what each of the arguments are and what you can use.

### test_suite arguments

In the test_suite folder, we have custom arguments built in, so we can run our tests on the latest versions of our
software.
Below is a table of what arguments are available to you, and which directory they are required in. If you do not use
these, the tests in that folder will **always** error out if it requires what is below.
For example if you don't fill the apk_path -> all tests for mobile app on Android will error out.

| Argument       | Value                                                                                   | Default | Required by suite |
|----------------|-----------------------------------------------------------------------------------------|---------|-------------------|
| `--apk_path`   | Path to the APK File for mobile app                                                  | `None`  | `test_sgo`        |
| `--ipa_path`   | Path to the IPA File for mobile app                                                  | `None`  | `test_sgo`        |
| `--web_url`    | The URL for website                                                              | `None`  | `test_web`        |
| `--msix_path`  | Path to the msix file for desktop app                                     | `None`  | Not used yet      |
| `--pkg_path`   | Path to the pkg file for desktop app                                      | `None`  | Not used yet      |
| `--exe_path`   | Path to the exe file for legacy desktop applications                                    | `None`  | Not used yet      |
| `--dmg_path`   | Path to the dmg file for legacy desktop applications                                    | `None`  | Not used yet      |
| `--version_no` | Version number of the programs being tested - To be used by Mekhane to upload to portal | `None`  | Not used yet      |

Example of use:

```commandline
pytest C:\path\to\test_suite --apk_path path/to/apk --ipa_path path/to/ipa --web_url www.silhouetteamerica.com
```

### Other PyTest Arguments

#### X-Dist

X Dist enables a lot of extra functionality to PyTest in terms of new execution modes. In our suite we use this
primarily to have multiple works running the tests to speed up the execution of the tests.

| Argument | Value   | Description                                                                                                                                                                                                       |
|----------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-n`     | auto    | Create a number of workers equal to the number of physical CPUS in the machine and distribute the tests to the workers                                                                                            | 
| `-n`     | logical | Create a number of workers equal to the number of logical CPUS in the machine and distribute the tests to the workers, this requires psutil package to be installed. If this command fails, it defaults to "auto" |

##### XDist example use

```commandline
pytest C:\path\to\test_suite -n logical
```

#### Rerun failures

rerunfailures is another PyTest plugin we use that will automatically retry tests that have failed

Due to the nature of our applications, most of the test we will write will be considered `flaky`. 
This is a technical term that essentially means there is a fair chance that this test can fail.

| Argument       | Value         | Description                                                     |
|----------------|---------------|-----------------------------------------------------------------|
| --reruns       | 1 -> infinity | How many times PyTest should retry the test if it keeps failing |
| --reruns-delay | 1 -> infinity | How many seconds between each retry of a failed test            |

##### Rerun example use

```commandline
pytest C:\path\to\test_suite --reruns 2 --reruns-delay 2
```

#### Allure

In order to get an Allure report, you need to tell PyTest to generate an Allure report as it is running the tests. To do
this, you need to add the following to the pytest command line:

`--alluredir=path/to/results`

As an example, this will create an "allure-results" folder where you are running the command:

```commandline
pytest 'path/to/test_suite' --alluredir=allure-results
```

Once the test is complete, you will notice that the allure-results folder has been made.

##### Viewing the Allure report

You then have 1 of 2 options to view the report:

1. `allure serve /path/to/allure-results`
    - This will generate and open the allure report automatically
    - If you have called the folder `allure-results` **and** you are working in the same directory as that folder, you
      can just type `allure serve` and it will find that folder
2. `allure generate /path/to/allure/results`
    - This will generate the allure report for you, then you can open it at a later date. using
        - `allure open /path/to/allure-report`

Note: It might be useful for you to also add the `--clean` argument to the allure commands - this will delete any
existing reports generated in that location

```commandline
allure generate /path/to/allure/results --clean
```

## PyCharm run configuration

Note: If you are using PyCharm - you can run our tests in the IDE with these arguments pre-defined:

- Right-click on the folder
- Click `Modify Run Configuration...`
- Put the arguments above in the `Additional Arguments` field

After doing this, you should see in the top right something along the lines of `Python tests in test_suite`

Doing it this way will give you a little UI window at the bottom of the IDE which may help you filter some of the raw
results from the PyTest framework.

---

# Writing tests

## Allure decorators

In this readme we go into what you need to know about Allure decorators to write tests.

If you are curious about all the Allure decorators that are available, you can find this at:
`Testing/Smoke/Extra Info/Allure Decorators.MD`

### What is a decorator?

>A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are typically applied to functions, and they play a crucial role in enhancing or modifying the behavior of functions.

In our test suite, we have some custom decorators which allow us to decorate our tests with Allure Attributes to help format the allure report.

- allure_suite
- allure_story
- allure_attributes

**These decorators are a requirement** any tests without these decorators will automatically fail.

### Allure suite

In our case, we are essentially mimicking the internal test structure into a more readable format.

#### Suite variables

| Parameter Name | Parameter Value | Description                              |
|----------------|-----------------|------------------------------------------|
| Parent Suite   | parent_suite    | Name of the Application                  |
| Suite Name     | suite_name      | The name of the folder the test is in    |
| Sub Suite Name | sub_suite_name  | The name of the file the test is in      |
| Test Title     | test_title      | The title of the test (This is optional) |

**Example:**

```python
@allure_suite("website", "Design", "Add Shapes", "Add Square")
def test_add_square(web_driver_home):
```

Below is the test structure for the test: "test_add_square"

`test_suite.test_web.test_design.test_add_shapes#test_add_square`

Without the decorator, the above is what would be shown in the Allure report

However, if we put the decorator on top of the function of `test_add_square` like so:

The Allure report will now replace:

- `test_suite.test_web` with `website`
- `test_design` with `Design`
- `test_add_shapes` with `Add Shapes`
- `test_add_square` with `Add Square`

### Allure story

These attributes are all about organising tests to the `User Story`

What this will allow us to do in our Allure report is have organisational structure based on the features of our Application that is not linked to the file structure in `test_suite`

This structure will be visible in the `Behaviors` section in the report

#### Story variables

| Parameter Name | Parameter Value | Description                              |
|----------------|-----------------|------------------------------------------|
| Epic           | epic_name       | Name of the Application tested           |
| Feature        | feature_name    | Name of the feature                      |
| Story          | story_name      | What the user is doing with that feature |

**Example**

```python
@allure_story("website","Shapes","Adding Shapes")
def test_add_square(web_driver_home):
```

Similar to the user story, this will replace the file/folder structure in `test_suite`, but will completely reorganise the tests depending on the story.
This means that if we have different tests in 2 locations, say:

- Testing/Smoke/test_suite/test_web/test_design/test_add_shapes.py
- Testing/Smoke/test_suite/test_web/test_tickets/test_shapes.py

But the tests have the same story attributes, they will appear in the same place in the `behaviour` section

### Allure attributes

With allure, you can add many attributes to the tests you are writing. Obviously some of these are not needed for every test you write.
But three of them we consider a requirement when writing the test:

| Parameter Name | Parameter Value | Description                                                                  |
|----------------|-----------------|------------------------------------------------------------------------------|
| Description    | description     | Short sentance explaining what we're testing                                 |
| Tag            | tags            | Any tags that relate to the test                                             |
| Severity       | severity_level  | The severity level of the test (How important it is compared to other tests) |
| Owner          | writer          | Who has written the test                                                     |

**Example**

```python
@allure_attributes(
    "Test for adding a circle",
    ["Add Shapes","Circle"],
    allure.severity_level.BLOCKER,
    "Daniel Burgess"
)
def test_add_circle(web_driver_home):
```

Now in the example above you're seeing 2 different types of data being added to the decorator:

- `tag`: This is accepting a list of strings - this allows it to add multiple tags at once
- `allure.severity_level.`: This is a built-in function of Allure that sets the severity level of the test. You can use the following to set the severity (In order):
  - `allure.severity_level.BLOCKER`
  - `allure.severity_level.CRITICAL`
  - `allure.severity_level.NORMAL`
  - `allure.severity_level.MINOR`
  - `allure.severity_level.TRIVIAL`

### Other Allure decorators

There are some other attributes that you can add that are not required for every test. This section lists those which we might find useful in specific scenarios.
All of these are implemented as decorators, so like the ones above they go above the function definition.

#### Allure issue

```python
@allure.issue("URL_TO_CODEBASE_TICKET", "TICKET_NUMBER")
```

Allows you to link a ticket to the test you're writing

#### Allure link

```python
@allure.link("https://example.com", name="External Link")
```

Allows you to link any external page that might be relevant to the test

### Dynamic Allure attributes

With Allure, there are some attributes that Allure can set during runtime of the test, below are some which are commonly used.

#### Allure dynamic title

Like you may have guessed, this allows you to create the title dynamically during the running of the test.

This is great if you have tests which have parameters which you would like to be in the title. 

**Example**

```python
@pytest.mark.parametrize("strategy", ["mobile", "desktop"])
@pytest.mark.parametrize("category", ["performance", "accessibility", "best-practices", "seo"])
def test_pagespeed_insights(strategy, category, web_url):
    allure.dynamic.title(f'Testing {category} score on {strategy}')
```

In the snippet above, we are pulling the parameters for `strategy` and `category` and using them in the title

**Please note, that you cannot use any decorators that modifies the title of the test if you plan to use the dynamic title**

#### Allure dynamic tag

This allows you to add tags dynamically at runtime.

Unlike the dynamic title, you can use this with the allure decorators.
Meaning if you have parameterized tests, you can set tags for all variations, then have unique tags for each run.

**Example**

```python
@allure_attributes(
    "This is checking to see if the score for performance, accessibility, seo and best practices score a number higher than 90",
    ["Page Speed Insights"],
    allure.severity_level.TRIVIAL
)
@pytest.mark.parametrize("strategy", ["mobile", "desktop"])
@pytest.mark.parametrize("category", ["performance", "accessibility", "best-practices", "seo"])
def test_pagespeed_insights(strategy, category, web_url):
    allure.dynamic.tag(category,strategy)
```

In the example above you can see we added the tag `Page Speed Insights` at the decorator level.
Then we use the `allure.dynamic.tag` to add the `category` and `strategy` parameters as tags.

### Allure steps

With Allure, we are able to say in the report what is going on during the test. It helps others reading the report understand what your tests are doing. It can also help you understand where the test is breaking during debugging.

It is worth noting that Allure Steps will automatically nest into each other depending on when they are run in the script.

#### Step decorator

```python
@allure.step("Clicking on element")
def element_click(driver, by_type, finder_value, timeout=120):
    element = element_wait_visible_and_enabled(driver, by_type, finder_value, timeout)
    if element is not None:
        try:
            element.click()
            print("Element clicked.")
        except Exception as e:
            pytest.fail(f"Failed to click element: {str(e)}")
```

In the example above, you can see above the function we have a `@allure.step`

With this in place, whenever this function is called during the test, a step will be created in the main body of the test stating:

- The text in the decorator
- The parameters used in that function

Depending on what happens it will change colour in the allure report

- If the function runs fine: Green Tick
- If the function fails: Red X
- If the function breaks: Yellow

#### With Allure step

```python
@pytest.fixture
def web_driver_design(web_driver_home):

    with allure.step("Going to the design page"):
        element_click(web_driver_home, By.CSS_SELECTOR, ".grid:nth-child(1) > .grid > .h-full > .w-10")

    yield web_driver_home
    # Any additional teardown logic can be added here
```

Allure also allows us to make individual steps in our code, not just steps in our functions

This can be particularly useful if your test has large blocks of code which is all for achieving the same goal.
Or if the element you're clicking are not "Human readable"

In the example above, we are using the `allure.step` to explain the next line of code is going to click the button to go to the design page.

Anything that is nested in the `with` statement will be considered part of the step. Yes you can have nested `with allure.step` commands

Please note though that we **only** use the allure steps to explain what is happening in the test. We do not use it as a debug log... that's what loggers and prints are for.

## Test Logger

In this test suite we have implemented a logger which is a requirement for almost all the functions in the conftest.py files and the driver_functions.py file.
This logger is a requirement for the functions inside these files, it will error out if you do not send the test_logger to the functions.

### Adding the test_logger to tests.

You add the test_logger the same way you decide what web / mobile_driver to use, for example:

```python
def test_add_heart(web_driver_design, test_logger):
    assert True
```

That is it. With just this in place you will start seeing logs for setting up the drivers for your test.

#### Using the test logger

The Logger is mainly for SRT QA to debug when the tests / automated system if a test fails for any reason.
With this we are able to generate separate logs for each test we run, so we can see in detail what exactly is going on and where the issue could lie.

Like most logs, we have 5 levels of logging we can report (In order of severity):

| Argument | Usage                  | Description                                                                                                                                                                        |
|----------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CRITICAL | test_logger.critical() | When something goes wrong so terribly it stops the whole test suite from working                                                                                                   |
| ERROR    | test_logger.error()    | When something stops a test from running / a failure in what is considered the "_backend_" of the system                                                                           |
| WARNING  | test_logger.warning()  | When there is a problem, but it's not going to stop anything. For example a common warning you might see is the test didn't find a local Selenium Grid                             |
| INFO     | test_logger.info()     | When there is information that we think might be useful for SRT QA or those curious and reading the logs. Example might be a sentance explaining we're using a local Selenium Grid |
| DEBUG    | test_logger.debug()    | Any information / data which will be useful for debugging issues. Example can be showing the contents of the list of URLs to check to find a Selenium grid                         |

Key things to note here:

- Using any of these logs will generate a `log` file which will automatically be added to the test. This is the "raw" log that you would see in the console
- ERROR and CRITICAL will also produce a `stderr` file which will automatically be added to the test. This is the "raw" error output from Python and only spits out the error.
- There are 4 custom logs that will be attached to your tests **dependent** on what log was triggered
  - An critical log if any `CRITICAL` have been added log
    - This log will also contain any lower level logs that were added to the log
  - An error log if any `ERROR` have been added to the log
    - This log will also contain any lower level logs that were added to the log
  - A log of all `WARNING` that has been added to the log
  - An `INFO` log which will contain all the `DEBUG` and `INFO` logs added to the log

##### Driver Functions

When you use the `element_click` or `element_wait` functions, they now also require you to past the `test_logger` into them.

The key thing to note here is that you need to add the logger **at the end of all required params**

So for example, the params for `element_click` are: 

```python
def element_click(driver, by_type, finder_value, test_logger, timeout=120):
    print("Clicking elements")
```

You can see that the last one: `timeout` has an `=120` at the end of it.

Whenever a parameter has an `=` this is essentially saying that this parameter has a default value. But you can send a different value if required

For most cases you do not need to worry about this as its very unlikely you will be modifying default values.
Also for most IDE's it will tell you which parameter you're entering as your making the function.

but as an example:

```python
element_click(web_driver_design, By.ID, "imageId", test_logger, 500)

element_click(web_driver_design, By.ID, "imageId", test_logger)
```

##### In the tests

You can add the test_logger for your own tests as well, there is a table above with showing how to define what level to use and when.

Example:

```python
def test_add_square(web_driver_design, test_logger):
    test_logger.critical("HEADSHOT")
    test_logger.error("404 not found")
    test_logger.warning("DON'T OPEN, DEAD INSIDE")
    test_logger.info("All British tanks have tea making abilities")
    test_logger.debug("Sky is set to reflect the colour of the ocean")
```

An **_EXTREMELY_** useful feature in Python is the ability to format strings with objects being used.

There are multiple ways to do this. But the easiest way is with the `Python f string`.

Using this, you can dump really useful data into your logs. For example:

```python
import requests

def is_capability_supported(grid_url, capabilities, test_logger):
  response = requests.get(f"{grid_url}/status")
  response.raise_for_status()
  grid_status = response.json()
  
  test_logger.debug(f'Response from {grid_url}: {grid_status}')
```
You can see in both the response declaration and in the test_logger.debug we are formatting the grid_url and grid_status respectively.
For our case this will make the debug log look something like:

`[DEBUG] test_cameo5[ANDROID - 13 ]:conftest.py:99 - Response from http://Mekhane.local:4444: {{"Value:"{"ready": true,...}}} (2024-11-28 16:24:47.544468)`

If we were debugging an issue regarding connecting to the Selenium Grid. It is extremely useful in the log if we're able to see what `grid_url` and `grid_status` actually were at the time of failure