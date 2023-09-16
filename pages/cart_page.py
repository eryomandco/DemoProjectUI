from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure
from utilities.logger import Logger


"""Here placed class Cart page with locators, getters, actions 
and method for going to place order page"""


# Class of page

class CartPage(Base):

    # Locators

    xpath_name_product = "//span[@data-entity='basket-item-name']"
    xpath_place_order_button = "//button[@data-entity='basket-checkout-button']"
    xpath_remove_order = "//span[@class='basket-item-actions-remove']"

    # Getters

    def get_place_order_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_place_order_button)))

    def get_remove_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_remove_order)))

    # Actions

    def click_place_order_button(self):
        self.get_place_order_button().click()
        print('Place order button has clicked')

    def click_remove_order(self):
        self.get_remove_order().click()
        print('Remove order button has clicked')

    # Method to go to place order

    def place_order(self):
        with allure.step('place order'):
            Logger.add_start_step(method='place_order')
            self.get_current_url()
            self.click_place_order_button()
            self.assert_URL('https://bravo31.ru/order/')
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='place_order')