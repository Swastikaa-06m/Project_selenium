from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    """Create and configure the Chrome WebDriver."""

    chrome_options = Options()

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(5)

    return driver