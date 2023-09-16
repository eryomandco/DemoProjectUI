import pytest
from selenium import webdriver

"""Here placed an example of using fixtures. 
Instead of messages about start/finish tests and suits it may be any function.
Some projects may place here a function of start and quit browser."""


@pytest.fixture(scope='module')
def suite_wrap():
    print("Start Test Suit")
    yield
    print("Finish Test suit")


@pytest.fixture()
def function_wrap():
    print("before function")
    yield
    print('after function')