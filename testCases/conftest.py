from selenium import webdriver
import pytest

@pytest.fixture()
def setUp(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("Launching Chrome")
    elif browser=="fiirefox":
        driver=webdriver.Firefox()
        print("Launching Firefox")
    else:
        driver=webdriver.Edge()
        print("Launching Default browser Microsoft Edge")
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return  request.config.getoption("--browser")
