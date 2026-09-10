from selenium import webdriver

def main():
    driver = None
    try:
        #Start a Chrome browser session
        #Selenium Manager automatically handles the required driver.
        driver = webdriver.Chrome()

        #Open the required practice page
        driver.get("https://leetcode.com")
        
        #Display the page title and current URL.
        print("Page Title:", driver.title)
        print("Current Url:", driver.current_url)
        input("Please Enter to close the browser...")
    finally:
        if driver is not None:
            driver.quit()

if __name__ == "__main__":
    main()