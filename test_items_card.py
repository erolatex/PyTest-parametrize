import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_order_button_presence(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector(".btn-add-to-basket")


