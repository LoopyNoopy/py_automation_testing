Allure provides several decorators in Python to help categorize and document tests. These decorators allow you to add metadata and organizational structure to your tests, improving the clarity and usefulness of Allure reports.

Here is a list of commonly used Allure decorators in Python:

### 1. **@allure.epic**
   - **Purpose**: Categorizes tests under a high-level "epic" grouping.
   - **Example**:
     ```python
     @allure.epic("User Management")
     ```

### 2. **@allure.feature**
   - **Purpose**: Groups tests within a specific feature of an epic.
   - **Example**:
     ```python
     @allure.feature("User Registration")
     ```

### 3. **@allure.story**
   - **Purpose**: Further categorizes tests under a particular story within a feature.
   - **Example**:
     ```python
     @allure.story("Password Complexity")
     ```

### 4. **@allure.description**
   - **Purpose**: Adds a detailed description of the test.
   - **Example**:
     ```python
     @allure.description("This test validates the password complexity requirements.")
     ```

### 5. **@allure.title**
   - **Purpose**: Sets a custom title for the test in the Allure report.
   - **Example**:
     ```python
     @allure.title("Test user registration form validation")
     ```

### 6. **@allure.severity**
   - **Purpose**: Sets the severity level of a test.
   - **Levels**: `BLOCKER`, `CRITICAL`, `NORMAL`, `MINOR`, `TRIVIAL`.
   - **Example**:
     ```python
     @allure.severity(allure.severity_level.CRITICAL)
     ```

### 7. **@allure.issue**
   - **Purpose**: Links the test to an issue tracker.
   - **Example**:
     ```python
     @allure.issue("JIRA-1234", "Login page fails with 500 error")
     ```

### 8. **@allure.testcase**
   - **Purpose**: Links the test to an external test case management system.
   - **Example**:
     ```python
     @allure.testcase("TESTCASE-123", "Test user registration workflow")
     ```

### 9. **@allure.tag**
   - **Purpose**: Adds custom tags to a test, useful for filtering in the report.
   - **Example**:
     ```python
     @allure.tag("smoke", "user_management")
     ```

### 10. **@allure.label**
   - **Purpose**: Adds a custom label to a test. Useful when creating custom fields for filtering or categorizing in Allure reports.
   - **Example**:
     ```python
     @allure.label("owner", "QA Team")
     ```

### 11. **@allure.step**
   - **Purpose**: Defines a step within a test, which can be nested. Useful for detailed step-by-step tracing.
   - **Usage**: Can be used as a decorator for functions or as a context manager within a test.
   - **Example**:
     ```python
     @allure.step("Open login page")
     def open_login_page():
         # Code to open the login page
         pass
     
     # Or as a context manager
     with allure.step("Check login page title"):
         assert page.title == "Login"
     ```

### 12. **@allure.dynamic.title**
   - **Purpose**: Sets a dynamic title at runtime.
   - **Example**:
     ```python
     allure.dynamic.title("Runtime title for test")
     ```

### 13. **@allure.dynamic.description**
   - **Purpose**: Sets a dynamic description at runtime.
   - **Example**:
     ```python
     allure.dynamic.description("This description is set at runtime.")
     ```

### 14. **@allure.dynamic.label**
   - **Purpose**: Adds a dynamic label at runtime.
   - **Example**:
     ```python
     allure.dynamic.label("owner", "Dev Team")
     ```

### 15. **@allure.dynamic.link**
   - **Purpose**: Adds a dynamic link to a test (like issue, testcase, or custom link).
   - **Example**:
     ```python
     allure.dynamic.link("https://example.com/issue/123", name="Related issue")
     ```

### 16. **@allure.attachment**
   - **Purpose**: Adds an attachment (e.g., a file, screenshot, or log) to the Allure report. Can be used with files or strings.
   - **Usage**:
     ```python
     @allure.attachment("Screenshot", attachment_type=allure.attachment_type.PNG)
     def capture_screenshot():
         # Code to capture a screenshot
         return open("screenshot.png", "rb").read()
     ```
     