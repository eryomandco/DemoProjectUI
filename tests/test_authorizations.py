import pytest
from selenium import webdriver
from pages.main_page import MainPage
import allure

"""Here placed three authorization autotest. Order of launch, fixtures and Allure report are set"""


# Method authorization with correct login and password
@pytest.mark.order(3)
@allure.description('"test_correct_authorization_data" is the test that try auth with correct data')
def test_correct_authorization_data(function_wrap):
    driver = webdriver.Chrome()
    print('\nSTART TEST')

    mp = MainPage(driver)
    mp.authorization()


# Method authorization with wrong login
@pytest.mark.order(1)
@allure.description('"test_wrong_login" is the test that try auth with wrong login')
def test_wrong_login(suite_wrap):
    driver = webdriver.Chrome()
    print('\nSTART TEST')
    mp = MainPage(driver)
    mp.authorization_wrong_login()


# Method authorization with wrong password
@pytest.mark.order(2)
@allure.description('"test_wrong_password" is the test that try auth with wrong password')
def test_wrong_password(suite_wrap):
    driver = webdriver.Chrome()
    print('\nSTART TEST')
    mp = MainPage(driver)
    mp.authorization_wrong_password()
