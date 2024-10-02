import time

import allure
import config
import data
from pages.login_page import LoginPage
from conftest import driver
from pages.restore_password_page import RestorePasswordPage


class TestRestorePassword:

    @allure.title('Проверка возможности навигации со страницы авторизации к странице восстановления пароля')
    def test_navigation_from_login_page_to_restore_password_page_click_restore_password_button(self, driver):
        login_page = LoginPage(driver)

        login_page.open_login_page()
        login_page.click_restore_password_button()

        assert login_page.get_current_url() == f'{config.Urls.BASE_URL}{config.Urls.RESTORE_PASSWORD_PATH}'

    @allure.title('При вводе email в поле ввода эмейла и клике на кнопку восстановить открывается форма '
                  'восстановления пароля')
    def test_possible_to_restore_password(self, driver):
        restore_password_page = RestorePasswordPage(driver)

        restore_password_page.open_restore_password_first_page()
        restore_password_page.set_email_input(data.RestorePasswordData.registered_email)
        restore_password_page.click_restore_password_button()

        assert restore_password_page.check_restore_password_title_appeared()

    @allure.title('Поле ввода пароля становится активным при нажатии на кнопку показа пароля')
    def test_password_input_becomes_active_after_show_password_button_clicked(self, driver):
        restore_password_page = RestorePasswordPage(driver)

        restore_password_page.open_restore_password_first_page()
        restore_password_page.set_email_input(data.RestorePasswordData.registered_email)
        restore_password_page.click_restore_password_button()
        restore_password_page.click_show_password_button()

        assert restore_password_page.check_password_input_is_active()













