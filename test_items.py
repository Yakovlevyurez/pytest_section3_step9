import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    #time.sleep(30)
    browser.implicitly_wait(3)

    button = browser.find_elements_by_css_selector('.btn.btn-add-to-basket')
    assert button, 'There is no "Add to basket" button at this window'



