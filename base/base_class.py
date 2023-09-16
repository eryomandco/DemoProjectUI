import datetime
import os
from selenium.webdriver import ActionChains

"""Here placed Base class the basis for classes of internet pages"""


# Class of page

class Base():

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    # Method get current url

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    # Method assert word value

    def assert_word(self, word, result):
        value = word.text
        assert value == result
        print('Value of test word is correct!')

    # Method take screenshot

    def screenshot(self):
        screenshot_folder = os.path.join('.', 'screenshots', '')
        current_time = datetime.datetime.now().strftime("%y-%m-%d_%H.%M.%S")
        name_screenshot = str(current_time) + '.png'
        self.driver.save_screenshot(screenshot_folder + name_screenshot)
        print('Screenshot has done!')
        return

    # Method assert URL

    def assert_URL(self, result):
        value = self.driver.current_url
        assert value == result
        print('Value of test URL is correct!')
