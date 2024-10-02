import allure

import config
import data
import locators
from pages.base_page import BasePage


class PersonalCabinetPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def open_personal_cabinet_page(self):
        self.open_page(f'{config.Urls.BASE_URL}{config.Urls.PERSONAL_CABINET_PATH}')

    def open_main_page(self):
        self.open_page(f'{config.Urls.BASE_URL}')

    def click_header_personal_cabinet_button_main_page(self):
        header_personal_cabinet_main_page_button = self.wait_and_find_element(locators.PersonalCabinetLocators.HEADER_PERSONAL_CABINET_BUTTON_LOCATOR)
        header_personal_cabinet_main_page_button.click()

    def set_access_token_to_session(self, access_token):
        self.set_access_token(access_token)

    def set_refresh_token_to_session(self, refresh_token):
        self.set_refresh_token(refresh_token)

    def check_logout_button_appeared(self):
        logout_button = self.wait_and_find_element(locators.PersonalCabinetLocators.LOGOUT_BUTTON_LOCATOR)
        return logout_button


    def click_orders_history_button(self):
        orders_history_button = self.wait_and_find_element(locators.PersonalCabinetLocators.ORDER_HISTORY_BUTTON_LOCATOR)
        orders_history_button.click()

    def click_logout_button(self):
        logout_button = self.wait_and_find_element(locators.PersonalCabinetLocators.LOGOUT_BUTTON_LOCATOR)
        logout_button.click()


    def check_login_title_appeared(self):
        login_title = self.wait_and_find_element(locators.PersonalCabinetLocators.LOGIN_TITLE_LOCATOR)
        return login_title

