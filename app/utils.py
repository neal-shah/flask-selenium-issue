from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import logging


def get_driver():
    logging.debug('Starting WebDriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    logging.debug('Starting Chrome')
    driver = webdriver.Chrome(chrome_options=options)
    driver.set_page_load_timeout(60)
    logging.debug('Starting Remote')
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )
    return driver


def connect_to_base(browser, page_number):
    base_url = f'https://news.ycombinator.com/news?p={page_number}'
    logging.debug(base_url)
    connection_attempts = 0
    while connection_attempts < 3:
        try:
            logging.debug('Getting URL')
            browser.get(base_url)
            # wait for table element with id = 'hnmain' to load
            # before returning True
            WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.ID, 'hnmain'))
            )
            return True
        except Exception as ex:
            connection_attempts += 1
            print(f'Error connecting to {base_url}.')
            print(f'Attempt #{connection_attempts}.')
    return False

