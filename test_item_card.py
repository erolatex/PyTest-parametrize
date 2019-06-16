import time
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_order_button_presence(browser):
    browser.get(link)
    #time.sleep(30)
   
    basket_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert EC.visibility_of(basket_button), "Basket button isn't visible or missing"
