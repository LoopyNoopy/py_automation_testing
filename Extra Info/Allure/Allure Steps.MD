Allure steps are used to structure test execution into logical steps, which are displayed in the Allure report. Steps make it easier to understand the flow of a test case and to pinpoint where an issue occurred.

You can use Allure steps in two ways:
1. As a **decorator** for functions or methods.
2. As a **context manager** for specific blocks of code.

---

### Example of Using Allure Steps

#### 1. **Using Steps as a Decorator**

```python
import allure

@allure.step("Open login page")
def open_login_page():
    # Simulate opening the login page
    print("Login page opened")

@allure.step("Enter username: {username}")
def enter_username(username):
    # Simulate entering a username
    print(f"Username entered: {username}")

@allure.step("Enter password: {password}")
def enter_password(password):
    # Simulate entering a password
    print("Password entered: [hidden]")

@allure.step("Click login button")
def click_login():
    # Simulate clicking the login button
    print("Login button clicked")

@allure.step("Verify login result")
def verify_login(expected_message):
    # Simulate login verification
    actual_message = "Welcome, user!"  # Replace with actual logic
    assert actual_message == expected_message, "Login verification failed"
    print("Login successful")
```

**Test Case Using Decorated Steps:**

```python
def test_login():
    open_login_page()
    enter_username("test_user")
    enter_password("secure_password")
    click_login()
    verify_login("Welcome, user!")
```

#### 2. **Using Steps as a Context Manager**

Steps can also be used for specific blocks of code:

```python
import allure

def test_search():
    with allure.step("Open search page"):
        # Simulate opening the search page
        print("Search page opened")
    
    with allure.step("Enter search query: 'Allure Reports'"):
        # Simulate entering a search query
        search_query = "Allure Reports"
        print(f"Search query entered: {search_query}")
    
    with allure.step("Click search button"):
        # Simulate clicking the search button
        print("Search button clicked")
    
    with allure.step("Verify search results"):
        # Simulate verifying search results
        search_results = ["Allure Report Guide", "Allure Report Examples"]
        assert "Allure Report Guide" in search_results, "Search results verification failed"
        print("Search results verified")
```

---

### How Steps Appear in Allure Reports

When the tests are run and the Allure report is generated, steps will appear hierarchically under each test case. Each step:
- Will be shown as a collapsible item.
- Will display its name (`@allure.step` or the `with allure.step(...)` string).
- Can show dynamic values (e.g., `{username}` or `{password}`) formatted in the step name.

---

### Run the Test with Allure

1. **Run the tests**:
   ```bash
   pytest --alluredir=allure-results
   ```

2. **Generate and view the report**:
   ```bash
   allure serve allure-results
   ```

You will see all steps with their respective details, making the report structured and easy to understand.