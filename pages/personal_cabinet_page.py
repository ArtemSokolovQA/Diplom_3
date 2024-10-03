import allure

import config
import locators
from pages.base_page import BasePage


class PersonalCabinetPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.title('Перейти на страницу личного кабинета')
    def open_personal_cabinet_page(self):
        self.open_page(f'{config.Urls.BASE_URL}{config.Urls.PERSONAL_CABINET_PATH}')

    @allure.title('Перейти на главную страницу')
    def open_main_page(self):
        self.open_page(f'{config.Urls.BASE_URL}')

    @allure.title('Нажать на кнопку личного кабинета в хедере страницы')
    def click_header_personal_cabinet_button_main_page(self):
        header_personal_cabinet_main_page_button = self.wait_and_find_element(locators.PersonalCabinetLocators.HEADER_PERSONAL_CABINET_BUTTON_LOCATOR)
        header_personal_cabinet_main_page_button.click()

    @allure.title('Установить авторизационный токен сессии')
    def set_access_token_to_session(self, access_token):
        self.set_access_token(access_token)

    @allure.title('Установить рефреш токен сессии')
    def set_refresh_token_to_session(self, refresh_token):
        self.set_refresh_token(refresh_token)

    @allure.title('Проверка появления кнопки выйти в личном кабинете пользователя')
    def check_logout_button_appeared(self):
        logout_button = self.wait_and_find_element(locators.PersonalCabinetLocators.LOGOUT_BUTTON_LOCATOR)
        return logout_button

    @allure.title('Нажать на кнопку история заказов в личном кабинете пользователя')
    def click_orders_history_button(self):
        orders_history_button = self.wait_and_find_element(locators.PersonalCabinetLocators.ORDER_HISTORY_BUTTON_LOCATOR)
        orders_history_button.click()

    @allure.title('Нажать на кнопку выйти на странице личного кабинета пользователя')
    def click_logout_button(self):
        logout_button = self.wait_and_find_element(locators.PersonalCabinetLocators.LOGOUT_BUTTON_LOCATOR)
        logout_button.click()

    @allure.title('Проверить, что появился заголовок войти')
    def check_login_title_appeared(self):
        login_title = self.wait_and_find_element(locators.PersonalCabinetLocators.LOGIN_TITLE_LOCATOR)
        return login_title

