from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure
from utilities.logger import Logger


"""Here placed class Cologne Product page with locators, getters, actions 
and method for add product to cart ang go to there page"""


# Class of page

class CologneProductPage(Base):

    # Locators

    xpath_product_name = "//h1[@id='pagetitle']"
    xpath_product_price = "//div[contains(@class, 'left_block')]//span[@class='price_value'][text()='484']"
    xpath_button_add_to_cart = "//div[@id='bx_117848907_53197_basket_actions']"
    xpath_cart_button = "//div[@class='wrap_icon wrap_basket baskets line-block__item top_basket']"

    # Getters

    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_product_price)))

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.xpath_button_add_to_cart)))

    def get_cart_bage(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_cart_button)))

    # Actions

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()

    def click_cart_button(self):
        self.get_cart_bage().click()

    # Method to add product to cart

    def add_product_to_cart(self):
        with allure.step('add product to cart'):
            Logger.add_start_step(method='add_product_to_cart')
            self.get_current_url()
            self.assert_word(self.get_product_name(), 'НЗ одеколон Арбат 100мл')
            self.click_button_add_to_cart()
            self.click_cart_button()
            self.assert_URL('https://bravo31.ru/basket/')
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='add_product_to_cart')