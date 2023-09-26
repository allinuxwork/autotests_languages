from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestCase:
    def test_add_to_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(5)

        button_text = browser.find_element(
            By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"
        )
        assert button_text, "button not found"
