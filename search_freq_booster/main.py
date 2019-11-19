from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webdriver_util
import threading


def get_keywords():
    keywords = []
    while True:
        keyword = input("Input keyword (input -1 to stop): ")
        if keyword is None:
            continue
        elif keyword == "-1":
            break
        else:
            keywords.append(keyword)

    if len(keywords) > 0:
        print("List of search keywords: ")
        for keyword in keywords:
            keyword_display = str("- {}").format(keyword)
            print(keyword_display)
    
    return keywords

def boost_search_freq(keyword):
    try:
        driver = webdriver_util.create_driver()
        while True:
            driver.get("http://google.com")
            search_box = driver.find_element_by_xpath("//input[@name='q']")
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.RETURN)
            webdriver_util.reset_driver(driver)      
    finally:
        webdriver_util.quit_driver(driver)


def main():
    keywords = get_keywords()

    print("Start boosting search frequency . . . . . . ")

    thread_pool = []

    for keyword in keywords:
        thread = threading.Thread(target = boost_search_freq, args = (keyword,))
        thread.start()
        thread_pool.append(thread)
    
    for thread in thread_pool:
        thread.join     

    

if __name__ == '__main__':
    main()