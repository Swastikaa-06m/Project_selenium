from operator import contains
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

driver.get("https://testautomationpractice.blogspot.com")

######
#Absolute Xpath
#/html/body/div/form/input

#Relative XPath
#//input[@id='email']
######
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@example.com")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Swastika Mondal")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("1234567890")
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("123 Main Street")


driver.find_element(By.XPATH, "//input[@id='female']").click()
driver.find_element(By.XPATH, "//input[@id='monday']").click()


country_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
country_dropdown.select_by_visible_text("India")

colors_listbox = Select(driver.find_element(By.XPATH, "//select[@id='colors']"))
colors_listbox.select_by_visible_text("Blue")

sorted_list = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))
sorted_list.select_by_visible_text("Cheetah")

# Date Picker 1
date_picker_1 = driver.find_element(
    By.XPATH, "//input[@id='datepicker']"
)

date_picker_1.click()

# Select a date from Date Picker 1
driver.find_element(
    By.XPATH,
    "//table[contains(@class,'ui-datepicker-calendar')]//a[text()='10']"
).click()

# Date Picker 2
date_picker_2 = driver.find_element(
    By.XPATH, "//input[@id='txtDate']"
)

date_picker_2.click()

driver.find_element(
    By.XPATH,
    "//table[contains(@class,'ui-datepicker-calendar')]//a[text()='6']"
).click()

start_date = driver.find_element(By.XPATH, "//input[@type='date'][1]")
end_date = driver.find_element(By.XPATH, "//input[@type='date'][2]")

driver.execute_script(
    "arguments[0].value = '2026-10-01';",
    start_date
)

driver.execute_script(
    "arguments[0].value = '2026-10-15';",
    end_date
)

input("Press Enter to close the browser...")
driver.quit()