from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))
elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose 'chrome' or 'firefox'")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#radio buttons
driver.find_element(By.CSS_SELECTOR, "input[value='radio1']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='radio2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='radio3']").click()

#name
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Swastika")

#checkboxes
driver.find_element(By.CSS_SELECTOR, "input[value='option1']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='option2']").click()
driver.find_element(By.CSS_SELECTOR, "input[value='option3']").click()

#dropdown-example
driver.find_element(By.CSS_SELECTOR, "select#dropdown-class-example option[value='option2']").click()

#country_selector
country = driver.find_element(By.CSS_SELECTOR, "#autocomplete").send_keys("India")

#password_example
password = driver.find_element(By.CSS_SELECTOR, "#displayed-text").send_keys("123456")

input("Press Enter to close the browser...")
driver.quit()