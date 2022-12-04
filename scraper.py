import sys
import re
import json
import threading
from time import sleep
from selenium import webdriver


def get_driver():  
    # initialize driver
    driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.ChromeOptions())
    return driver


def thread_function(tno):
    print("Starting thread " + str(tno))
    browser = get_driver()
    print(f'Scraping page...')
    browser.get("http://www.google.com")
    html = browser.page_source
    print("RESULT ++++++++++++++++++++++++++++++++++++++++++++++")
    print(html)
    browser.quit()
    print(f'Finished and releasing the browser! #' + str(tno))


if __name__ == '__main__':
    t = []
    for i in range(20):
        t.append(threading.Thread(target=thread_function, args=(i,)))
    
    for i in range(20):
        t[i].start()

    # if need to wait all done
    #for i in range(20):
    #    t[i].join()
