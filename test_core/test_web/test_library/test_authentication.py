import pytest
import allure

pytestmark = pytest.mark.library


@pytest.fixture(scope="function", autouse=True)
def set_suite():
    allure.suite("Authentication")


@allure.title("Signin attempt with valid emails and passwords")
@allure.story("User Login")
@allure.description("This test verifies if a user can sign in")
@pytest.mark.beta
def test_sign_in_valid_credentials(web_driver):  # ToDo - Write test
    assert False
