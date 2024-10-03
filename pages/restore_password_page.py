import allure

import config
import data
import locators
from pages.base_page import BasePage

class RestorePasswordPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step('Перейти на страницу восстановления пароля')
    def open_restore_password_first_page(self):
        self.open_page(f'{config.Urls.BASE_URL}{config.Urls.RESTORE_PASSWORD_PATH}')

    def open_restore_password_second_page(self):
        self.open_page(f'{config.Urls.BASE_URL}{config.Urls.RESET_PASSWORD_PATH}')

    @allure.step('Заполнить поле email на странице восстановления пароля')
    def set_email_input(self, email):
        self.set_input(locators.RestorePasswordLocators.EMAIL_INPUT_LOCATOR, email)

    @allure.step('Кликнуть по кнопке "Восстановить" в форме восстановления пароля')
    def click_restore_password_button(self):
        restore_password_button = locators.RestorePasswordLocators.RESTORE_PASSWORD_BUTTON_LOCATOR
        self.click_element(restore_password_button)

    @allure.step('Проверить, что появился заголовок "Восстановление пароля"')
    def check_restore_password_title_appeared(self):
        restore_password_title = self.wait_and_find_element(locators.RestorePasswordLocators.RESTORE_PASSWORD_TITLE_LOCATOR)
        return restore_password_title

    @allure.title('Нажать на кнопку показа пароля')
    def click_show_password_button(self):
        show_password_button = self.wait_and_find_element(locators.RestorePasswordLocators.SHOW_PASSWORD_BUTTON_LOCATOR)
        show_password_button.click()

    @allure.title('Проверить, что поле ввода пароля стало активным')
    def check_password_input_is_active(self):
        active_password_input = self.wait_and_find_element(locators.RestorePasswordLocators.FOCUSED_PASSWORD_INPUT)
        return active_password_input

