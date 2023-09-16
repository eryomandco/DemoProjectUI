from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure
from utilities.logger import Logger


"""Here placed class For Men page with locators, getters, actions 
and method for sorting products and going to chosen Product page"""


# Class of page

class ForMenPage(Base):

    # Locators

    xpath_price_button = "//div[text()='Цена']"
    xpath_price_slider_left = "//a[@id='left_slider_MAX']"
    xpath_price_slider_right = "//a[@id='right_slider_MAX']"
    xpath_brand_button = "//span[text()='Бренд']"
    xpath_brand_checkbox = "//label[@data-role='label_MAX_SMART_FILTER_932_1317358923']"
    xpath_type_skin_button = "//span[text()='Тип кожи']"
    xpath_type_skin_checkbox = "//label[@data-role='label_MAX_SMART_FILTER_960_2616966098']"
    xpath_country_button = "//span[text()='Страна производства']"
    xpath_country_checkbox = "//label[@for='MAX_SMART_FILTER_938_1734330656']"
    xpath_sort_button = "//div[@class='dropdown-select__title font_xs darken']" \
                        "//span[text()[normalize-space()='По алфавиту (возрастание)']]"
    xpath_button_price_low_to_high = "//div[@class='dropdown-select__list-item font_xs']" \
                                     "//span[text()[normalize-space()='По цене (возрастание)']]"
    xpath_product_card_cologne = "//div[@class='item-title']//span[text()='НЗ одеколон Арбат 100мл']"

    # Getters

    def get_price_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_price_button)))

    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_price_slider_left)))

    def get_price_slider_right(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_price_slider_right)))

    def get_brand_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_brand_button)))

    def get_brand_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_brand_checkbox)))

    def get_type_skin_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_type_skin_button)))

    def get_type_skin_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.xpath_type_skin_checkbox)))

    def get_country_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_country_button)))

    def get_country_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_country_checkbox)))

    def get_sort_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_sort_button)))

    def get_button_price_low_to_high(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.xpath_button_price_low_to_high)))

    def get_product_card_cologne(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.xpath_product_card_cologne)))

    # Actions

    def click_price_button(self):
        self.get_price_button().click()
        print('Price button has clicked')

    def click_and_pull_left_slider(self, ):
        self.action.click_and_hold(self.get_price_slider_left()).move_by_offset(10, 0).release().perform()
        print('Left slider has clicked and moved to right')

    def click_and_pull_right_slider(self):
        self.action.click_and_hold(self.get_price_slider_right()).move_by_offset(-100, 0).release().perform()
        print('Right slider has clicked and moved to left')

    def click_brand_button(self):
        self.get_brand_button().click()
        print('Brand button has clicked')

    def click_brand_checkbox(self):
        self.get_brand_checkbox().click()
        print('Brand checkbox has clicked')

    def click_country_button(self):
        self.get_country_button().click()
        print('Country button has clicked')

    def click_country_checkbox(self):
        self.get_country_checkbox().click()
        print('Country checkbox has clicked')

    def click_type_skin_button(self):
        self.get_type_skin_button().click()
        print('Type skin button has clicked')

    def click_type_skin_checkbox(self):
        self.get_type_skin_checkbox().click()
        print('Type skin checkbox has clicked')

    def click_sort_button(self):
        self.get_sort_button().click()
        print('Sort button has clicked')

    def click_button_price_low_to_high(self):
        self.get_button_price_low_to_high().click()
        print('Button to sort by ascending has clicked')

    def click_product_card_cologne(self):
        self.get_product_card_cologne().click()
        print('Product card of cologne has clicked')

    # Method to sort price and choose product that you like

    def sort_price_and_choose_product(self):
        with allure.step('sort price and choose product'):
            Logger.add_start_step(method='sort_price_and_choose_product')
            self.get_current_url()
            self.click_price_button()
            self.click_and_pull_left_slider()
            self.click_and_pull_right_slider()
            self.click_brand_button()
            self.click_brand_checkbox()
            self.click_country_button()
            self.click_country_checkbox()
            self.click_type_skin_button()
            self.click_type_skin_checkbox()
            self.click_sort_button()
            self.click_button_price_low_to_high()
            try:
                self.click_product_card_cologne()
                print('First attempt is good')
            except StaleElementReferenceException:
                self.click_product_card_cologne()
                print('Second attempt is good')
            self.assert_URL('https://bravo31.ru/catalog/_parfyumeriya/dlya_muzhchin_2/53197/')
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='sort_price_and_choose_product')