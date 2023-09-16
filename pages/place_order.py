from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.cart_page import CartPage
import allure
from utilities.logger import Logger


"""Here placed class Place Order page with locators, getters, actions 
and method for clear and fill city address field, then go to Cart page, delete order and refresh page"""


# Class of page

class PlaceOrder(Base):

    # Locators

    xpath_deselect_button = '//div[@style="display: block;"]'
    xpath_location_field = '//div[@class="bx-ui-sls-container"]//input[@value="0000133095"]'
    xpath_choice_location = '//div[@class="dropdown-item bx-ui-sls-variant bx-ui-sls-variant-active"]'
    xpath_cart = '//div[@id="bx-soa-total"]//a[@href="/basket/"]'

    # Getters

    def get_deselect_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.xpath_deselect_button)))

    def get_location_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_location_field)))

    def get_choice_location(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_choice_location)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_cart)))

    # Actions

    def click_deselect_button(self):
        self.get_deselect_button().click()
        print('Cancel choice button has clicked')

    def fill_location_field(self):
        self.get_location_field().send_keys("Белгород")
        self.get_location_field().send_keys(Keys.ENTER)
        print('Location field got: Белгород')

    def click_choice_location(self):
        self.get_choice_location().click()
        print('Location has chosen')

    def click_cart(self):
        self.get_cart().click()
        print('Cart has clicked')

    # Method to place and remove order

    def place_and_remove_order(self):
        with allure.step('place and remove order'):
            Logger.add_start_step(method='place_and_remove_order')
            self.get_current_url()
            self.click_deselect_button()
            self.fill_location_field()
            self.click_choice_location()
            try:
                self.click_cart()
                print('First attempt is good')
            except StaleElementReferenceException:
                self.click_cart()
                print('Second attempt is good')
            CartPage.click_remove_order(CartPage(self.driver))
            self.driver.refresh()
            Logger.add_end_step(url=self.driver.current_url, method='place_and_remove_order')