import config
from pages.base_page import BasePage
from locators import LoginPageLocators
import allure


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step('Перейти на страницу /login')
    def open_login_page(self):
        self.open_page(f'{config.Urls.BASE_URL}{config.Urls.LOGIN_PATH}')

    @allure.step('Кликнуть по кнопке "Восстановить пароль"')
    def click_restore_password_button(self):
        restore_password_button = self.wait_and_find_element(LoginPageLocators.RESTORE_PASSWORD_BUTTON_LOCATOR)
        restore_password_button.click()

    # @allure.step('')






