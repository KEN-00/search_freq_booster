from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyword_helper
import webdriver_helper
import threading




def boost_search_freq(keyword):
    try:
        driver = webdriver_helper.create_driver()
        while True:
            driver.get("http://google.com")
            search_box = driver.find_element_by_xpath("//input[@name='q']")
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.RETURN)
            webdriver_helper.reset_driver(driver)      
    finally:
        webdriver_helper.quit_driver(driver)

def batch_boost_search_freq(keywords):
    print("Start boosting search frequency . . . . . . ")
    thread_pool = []
    for keyword in keywords:
        thread = threading.Thread(target = boost_search_freq, args = (keyword,))
        thread.start()
        thread_pool.append(thread)
    
    for thread in thread_pool:
        thread.join   


def main():
    keywords = keyword_helper.get_keywords_from_txt()
    batch_boost_search_freq(keywords) 


if __name__ == '__main__':
    main()