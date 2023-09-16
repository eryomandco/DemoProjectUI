from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure
from utilities.logger import Logger


"""Here placed class Perfume Page with locators, getters, actions 
and method for going to page For Men"""


# Class of page

class PerfumePage(Base):

    # Locators

    xpath_button_for_men = '//span[@class="font_md"][text()="Для мужчин"]'

    # Getters

    def get_button_for_men(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_button_for_men)))

    # Actions

    def click_button_for_men(self):
        self.get_button_for_men().click()
        print('Button FOR MEN has clicked')

    # Method go to page For Men

    def go_to_page_for_men(self):
        with allure.step('go to page for men'):
            Logger.add_start_step(method='go_to_page_for_men')
            self.get_current_url()
            self.click_button_for_men()
            self.assert_URL('https://bravo31.ru/catalog/_parfyumeriya/dlya_muzhchin_2/')
            Logger.add_end_step(url=self.driver.current_url, method='go_to_page_for_men')
