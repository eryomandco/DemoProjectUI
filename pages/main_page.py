from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import allure
from utilities.logger import Logger


"""Here placed test data and class Main Page with locators, getters, actions 
and authorization methods as well as method go to Perfume page"""


# Test data

base_url = 'https://bravo31.ru/'
base_login = 'foded33213@horsgit.com'
base_password = 'QAtester123'
wrong_login = 'foded33213@horsgit.co'
wrong_password = 'QAtester12'


# Class of page

class MainPage(Base):

    # Locators

    xpath_my_cabinet = '//div[contains(@class, "inner-table-block person")]'
    xpath_login_field = '//input[@id="USER_LOGIN_POPUP"]'
    xpath_password_field = '//input[@id="USER_PASSWORD_POPUP"]'
    xpath_enter_button = '//button[@name="Login1"]'
    xpath_login_successful_message = '//div[contains(@class, "notice__title")]'
    xpath_alarm_message = '//div[@class="alert alert-danger compact"]'
    xpath_perfume_button = '//a[@class="icons_fa parent rounded2 bordered"]//span[text()="  Парфюмерия"]'

    # Getters

    def get_my_cabinet_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_my_cabinet)))

    def get_login_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_login_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_password_field)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_enter_button)))

    def get_login_successful_message(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.xpath_login_successful_message)))

    def get_alarm_message(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                self.xpath_alarm_message)))

    def get_perfume_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.xpath_perfume_button)))

    # Actions

    def click_my_cabinet_button(self):
        self.get_my_cabinet_button().click()
        print('My cabinet button has clicked')

    def input_login(self, login_name):
        self.get_login_field().send_keys(login_name)
        print('Login has entered in the field')

    def input_password(self, password):
        self.get_password_field().send_keys(password)
        print('Password has entered in the field')

    def click_enter_button(self):
        self.get_enter_button().click()
        print('Enter button has clicked')

    # Method go to Perfume page

    def click_perfume_button(self):
        self.get_perfume_button().click()
        print('Perfume button has clicked')
        self.assert_URL('https://bravo31.ru/catalog/_parfyumeriya/')

    # Authorization methods

    def authorization(self):
        with allure.step('authorization'):
            Logger.add_start_step(method='authorization')
            self.driver.get(base_url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_my_cabinet_button()
            self.input_login(base_login)
            self.input_password(base_password)
            self.click_enter_button()
            self.assert_word(self.get_login_successful_message(), 'Вы успешно авторизовались')
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='authorization')

    def authorization_wrong_login(self):
        with allure.step('authorization wrong login'):
            Logger.add_start_step(method='authorization_wrong_login')
            self.driver.get(base_url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_my_cabinet_button()
            self.input_login(wrong_login)
            self.input_password(base_password)
            self.click_enter_button()
            self.assert_word(self.get_alarm_message(), 'Неверный логин или пароль.')
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='authorization_wrong_login')

    def authorization_wrong_password(self):
        with allure.step('authorization wrong password'):
            Logger.add_start_step(method='authorization_wrong_password')
            self.driver.get(base_url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_my_cabinet_button()
            self.input_login(base_login)
            self.input_password(wrong_password)
            self.click_enter_button()
            self.assert_word(self.get_alarm_message(), 'Неверный логин или пароль.')
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='authorization_wrong_password')