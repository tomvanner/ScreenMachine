import time
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebScreenshot:
    def __init__(self, driver_path):
        chrome_options = self.__get_options()
        self.driver = webdriver.Chrome(driver_path, options=chrome_options)
    
    def __get_options(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--start-maximized')

        return options

    def get_screenshot_uri(self, url):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        url_parse = urlparse(url)

        screenshot_filename = (
            "screenshot-{url}-{timestamp}.png"
            .format(url=url_parse.netloc, timestamp=timestamp)
        )

        self.driver.get(url)

        ele=self.driver.find_element("xpath", '//body')
        total_height = ele.size["height"]

        self.driver.set_window_size(1920, 1080)

        self.driver.save_screenshot(screenshot_filename)
        self.driver.quit()

        return screenshot_filename
