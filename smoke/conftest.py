import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import target_config
import os
import allure
from allure.constants import AttachmentType

browserstack_executor = os.getenv("BROWSERSTACK_EXECUTOR")


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    allure.environment(
        test_url=os.getenv("TEST_URL") or 'www.schireson.com'
    )


@pytest.fixture
def get_webdriver(device):
    desired_capabilities = target_config.options[device]

    desired_capabilities['pageLoadStrategy'] = "none"
    # Set networkLogs to True to enable download network log through api
    # desired_capabilities['browserstack.networkLogs'] = "true"
    desired_capabilities[
            'browserstack.localIdentifier'] = os.environ.get(
                "BROWSERSTACK_LOCAL_IDENTIFIER")

    # TODO: replace your browserstack username and token on ENV variable
    return webdriver.Remote(
        command_executor=browserstack_executor,
        desired_capabilities=desired_capabilities
    )


@pytest.fixture
def driver(device):
    if browser_flag().lower() != 'n':
        driver_instance = get_webdriver(device)
    if browser_flag().lower() == 'n':
        caps = DesiredCapabilities.CHROME
        caps["pageLoadStrategy"] = "none"
        caps["version"] = "65.0"
        caps["browserName"] = "chrome"
        driver_instance = webdriver.Chrome(desired_capabilities=caps)
    try:
        yield driver_instance
    finally:
        console_log = driver_instance.get_log('browser')
        allure.attach('console log', str(console_log))
        allure.attach(
            'screenshot',
            driver_instance.get_screenshot_as_png(),
            type=AttachmentType.PNG
        )
        allure.environment(browser=driver_instance.desired_capabilities[
            'browserName'] + ' ' +
            driver_instance.desired_capabilities['version'])
        driver_instance.quit()


@pytest.fixture
def browser_flag():
    "pytest fixture for browser"
    return pytest.config.getoption("-B")


@pytest.fixture
def device():
    "pytest fixture for cap initial"
    return


def pytest_generate_tests(metafunc):
    "test generator function to run tests across different parameters"
    if 'device' in metafunc.fixturenames:
        if metafunc.config.getoption("-B").lower() == "all":
            metafunc.parametrize(
                "device",
                target_config.cross_all_browser_config)
        elif metafunc.config.getoption("-B").lower() == "mobile":
            metafunc.parametrize(
                "device",
                target_config.cross_mobile_browser_config)
        elif metafunc.config.getoption("-B").lower() == "web":
            metafunc.parametrize(
                "device",
                target_config.cross_web_browser_config)
        else:
            if metafunc.config.getoption("-B").lower() != "n":
                i = metafunc.config.getoption("-B")
                test_config = []
                test_config.append(i)
                metafunc.parametrize(
                    "device",
                    test_config)


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="N",
                     help="Browser. Valid options are " +
                          "All, mobile, web and specific option")
