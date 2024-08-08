import time

import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Booking(webdriver.Chrome):
    def __init__(self, options, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        # this 1 second is necessary to let page load
        time.sleep(1)

        WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'))
        )
        currency_element = self.find_element(
            "css selector",
            'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        WebDriverWait(self, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="selection-item"]'))
        )
        currency_button = self.find_element(
            By.XPATH, f'//div[@class=" b284c0e8fc" and text()="{currency}"]/ancestor::button'
        )
        currency_button.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(by=By.ID, value=':rh:')
        search_field.clear()
        search_field.send_keys(place_to_go)

        # Wait for search bar to expend
        # i know there is smarter way to do it ;)
        time.sleep(1)

        first_result = self.find_element(by=By.ID, value='autocomplete-result-0')
        first_result.click()

    # Fix me
    def select_dates(self, check_in_date='2024-08-22', check_out_date='2024-08-31'):
        check_in_element_child = self.find_element(by=By.CSS_SELECTOR, value=f'span[data-date="{check_in_date}"]')
        check_in_element = check_in_element_child.find_element(By.XPATH, "./ancestor::td")
        print(check_in_element_child.get_attribute("class"))
        check_in_element_child.click()

        #check_out_element = self.find_element(by=By.CSS_SELECTOR, value=f'span[data-date="{check_out_date}"]')
        #check_out_element.click()