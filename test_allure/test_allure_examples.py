import pytest
import allure

#https://allurereport.org/docs/frameworks/python/pytest/
#https://medium.com/testvagrant/generating-allure-reports-in-the-pytest-framework-89dc78a2ca85
#pytest --alluredir=allure-results test_allure_examples.py
#npx allure serve allure-results

@allure.epic("Web interface")
@allure.feature("Essential features")
@allure.story("Authentication")
@allure.parent_suite("Tests for web interface")
@allure.suite("Tests for essential features")
@allure.sub_suite("Tests for authentication")
@pytest.mark.category("Chicken")
@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 3), (2, 3, 5), (5, 5, 10)])
def test_addition(num1, num2, expected):
    result = num1 + num2
    assert result == expected

@pytest.mark.category("Chicken")
@pytest.mark.slow
def test_slow_operation():
    # Your slow test code here
    value = 1
    assert value == 2
    pass
