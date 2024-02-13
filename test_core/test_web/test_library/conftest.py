import pytest
import allure


@pytest.fixture(scope="function", autouse=True)
def set_decorators():
    allure.parent_suite("Library Testing")
