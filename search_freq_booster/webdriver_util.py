from selenium import webdriver
import constant

def create_driver():
    driver = webdriver.Chrome(constant.CHROME_DRIVER_PATH)
    driver.delete_all_cookies()
    return driver

def quit_driver(driver):
    if driver != None:
        try:
            driver.quit()
        except:
            pass
    

def reset_driver(driver):
    if driver != None:
        try:
            driver.deleteAllCookies()
            driver.get("data:,")
        except:
            pass
