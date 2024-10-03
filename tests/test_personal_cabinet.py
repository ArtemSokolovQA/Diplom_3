import allure
import config
from conftest import driver, login
from pages.personal_cabinet_page import PersonalCabinetPage


class TestPersonalCabinet:

    @allure.title('Клик по кнопке личного кабинета в хедере ведет на страницу личного кабинета')
    def test_click_header_personal_cabinet_button_navigates_to_personal_cabinet(self, driver, login):
        personal_cabinet_page = PersonalCabinetPage(driver)

        personal_cabinet_page.open_main_page()
        tokens = login
        personal_cabinet_page.set_access_token(tokens[0])
        personal_cabinet_page.click_header_personal_cabinet_button_main_page()

        assert personal_cabinet_page.check_logout_button_appeared()
        assert personal_cabinet_page.get_current_url() == f'{config.Urls.BASE_URL}{config.Urls.PERSONAL_CABINET_PATH}'

    @allure.title('Возможность перехода в раздел истории заказов пользователя')
    def test_navigation_to_orders_history_page(self, driver, login):
        personal_cabinet_page = PersonalCabinetPage(driver)
        tokens = login

        personal_cabinet_page.open_main_page()
        personal_cabinet_page.set_access_token(tokens[0])
        personal_cabinet_page.click_header_personal_cabinet_button_main_page()
        personal_cabinet_page.click_orders_history_button()

        assert personal_cabinet_page.get_current_url() == f'{config.Urls.BASE_URL}{config.Urls.ORDER_HISTORY_PATH}'

    @allure.title('Возможно выйти из учетной записи нажатием по кнопке выйти в личном кабинете')
    def test_logout(self, driver, login):
        personal_cabinet_page = PersonalCabinetPage(driver)
        tokens = login

        personal_cabinet_page.open_main_page()
        personal_cabinet_page.set_access_token(tokens[0])
        personal_cabinet_page.set_refresh_token(tokens[1])
        personal_cabinet_page.click_header_personal_cabinet_button_main_page()
        personal_cabinet_page.click_logout_button()

        assert personal_cabinet_page.check_login_title_appeared()
        assert personal_cabinet_page.get_current_url() == f'{config.Urls.BASE_URL}{config.Urls.LOGIN_PATH}'





