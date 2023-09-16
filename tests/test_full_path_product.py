from selenium import webdriver
from pages.cart_page import CartPage
from pages.cologne_product_page import CologneProductPage
from pages.for_men_page import ForMenPage
from pages.main_page import MainPage
from pages.perfume_page import PerfumePage
from pages.place_order import PlaceOrder
import allure

"""Test full business path from authorization to place order and delete it"""


# Method to test full business path

@allure.description('"test_full_path" is the test, whose does standard user path from login to place order')
def test_full_path():
    driver = webdriver.Chrome()
    print('\nSTART TEST')

    # Method authorization
    mp = MainPage(driver)
    mp.authorization()
    # Method go to page Perfume
    mp.click_perfume_button()

    # Method go to page For Men
    pp = PerfumePage(driver)
    pp.go_to_page_for_men()

    # Method sort product by price, country, brand, skin, price range and go to Cologne Product page
    fmp = ForMenPage(driver)
    fmp.sort_price_and_choose_product()

    # Method add product to cart and go to Cart page
    cpp = CologneProductPage(driver)
    cpp.add_product_to_cart()

    # Method confirm order and go to Place Order page
    cp = CartPage(driver)
    cp.place_order()

    # Method place order, choose city and delete product
    po = PlaceOrder(driver)
    po.place_and_remove_order()