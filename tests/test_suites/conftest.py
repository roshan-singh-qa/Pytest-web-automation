import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver: ChromeDriverManager = None


def get_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument('--disable-web-security')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-insecure-localhost')  # differ on driver version. can ignore.
    caps = options.to_capabilities()
    caps["acceptInsecureCerts"] = True
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), desired_capabilities=caps)
    return driver


@pytest.fixture(scope="class", autouse=True)
def setup(request, browser):
    print("Running one time setUp")
    driver = get_chrome()
    url = 'https://www.javatpoint.com/'
    try:
        driver.get(url)
        if request.cls is not None:
            request.cls.driver = driver
        yield driver
    finally:
        driver.quit()
    print("\nRunning one time tearDown")


def pytest_addoption(parser):
    parser.addoption('--browser', default="Chrome", help="BH AD USERNAME")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


def test():
    print("This is for test")
