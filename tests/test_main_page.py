import allure
import config
from conftest import driver
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Клик по кнопке конструктор ведет на главную')
    def test_navigation_to_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_constructor_button()

        assert main_page.get_current_url() == f'{config.Urls.BASE_URL}{config.Urls.CONSTRUCTOR_PATH}'

    @allure.title('Навигация с главной страницы на страницу ленты')
    def test_navigation_from_main_page_to_feed(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_feed_button()

        assert main_page.get_current_url() == f'{config.Urls.BASE_URL}{config.Urls.FEED_PATH}'

    @allure.title('Открытие модального окна деталей об ингредиенте после клика по карточке ингредиента')
    def test_ingredient_details_modal_opens_after_click_ingredient_card(self, driver):

        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredients_card()

        assert main_page.check_ingredient_details_modal_appeared()

    @allure.title('Можно закрыть модальное окно деталей об ингредиенте нажатием на крестик')
    def test_ingredient_details_modal_closes_after_click_close_button(self, driver):

        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredients_card()
        main_page.click_close_ingredient_modal_button()

        assert main_page.check_ingredient_modal_is_closed()











