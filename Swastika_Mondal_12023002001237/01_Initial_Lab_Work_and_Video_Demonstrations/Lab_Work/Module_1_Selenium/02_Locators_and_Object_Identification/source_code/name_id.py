from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

#name
user = driver.find_element(By.ID, "username").send_keys("tomsmith")

#password
pswd = driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")

#tags
heading = driver.find_element(By.TAG_NAME, "h2").text
print(f"Heading: {heading}")

#link
link = driver.find_element(By.LINK_TEXT, "Elemental Selenium").get_attribute("href")
print(f"Link: {link}")

#button
btn = driver.find_element(By.CLASS_NAME, "radius").click()

input("Press Enter to close the browser...")
driver.quit()
