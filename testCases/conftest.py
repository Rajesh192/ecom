from selenium import webdriver
import pytest


@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# HTML REPORTS


def pytest_configure(config):
    config._metadata['Project Name'] = 'Ecom'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Rajesh'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
