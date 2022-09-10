import pytest
from selenium import webdriver
from pages.home.login_page import LoginPage


@pytest.fixture()
def setUp():
    print("Run conftest before every method setup")
    yield
    print("Run conftest after every method setup")


@pytest.fixture(scope="class")
def oneTimeSetup(request, browser):
    print("Running one time setup")

    # if loop for browser
    if browser == 'firefox':
        baseurl = "https://courses.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        print("Running test on firefox")
    else:
        baseurl = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        print("Incorrect browser")

    # Login to website
    # wdf = WebDriverFactory(browser)
    # driver = wdf.getWebDriverInstance()
    lp =LoginPage(driver)
    lp.login("abhijeetsutar@hotmail.com", "xyzxyz")

    # As per the syntax, there a cannot be 2 or more if loops for command line argruments in fixtures
    # # if loop for osType
    # if osType=='windows':
    #     print("Running test on windows")
    # else:
    #     print("Incorrect OS type")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    # driver.quit()
    print("Run ConfTest demo one time setup teardown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="test1334")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
