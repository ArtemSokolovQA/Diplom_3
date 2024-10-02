import time
import allure
import config
import data
from pages.order_feed_page import OrderFeedPage
from conftest import driver, login_and_create_order, login
from pages.main_page import MainPage
import locators
import requests


class TestOrderFeed:

    @allure.title('Открытие модального окна деталей о заказе после клика по карточке заказа')
    def test_order_details_opens_after_ingredient_card_clicked(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_order_feed_page()
        order_feed_page.click_order_card()

        assert order_feed_page.check_order_details_modal_is_opened()

    @allure.title('Заказ пользователя отображается в ленте заказов')
    def test_user_orders_are_presented_in_feed(self, driver, login_and_create_order):
        order_feed_page = OrderFeedPage(driver)
        order_number = login_and_create_order

        order_feed_page.open_order_feed_page()
        assert order_feed_page.check_order_number_in_order_card()[2:] == f'{order_number}'

    @allure.title('Счётчик всех выполненных заказов увеличивается после создания заказа')
    def test_orders_counter_increases_after_order_creation(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_order_feed_page()
        all_completed_orders_amount = int(order_feed_page.get_all_completed_orders_amount())

        auth_response = requests.post(f'{config.Urls.BASE_URL}{config.Urls.LOGIN_API_PATH}',
                                      json=data.LoginData.registered_user)
        access_token = auth_response.json().get('accessToken')
        auth_response.json().get('refreshToken')
        requests.post(f'{config.Urls.BASE_URL}{config.Urls.CREATE_ORDER_API_PATH}',
                      json=data.CreateOrderData.create_order_data, headers={
                'Authorization': access_token
            })
        order_feed_page.refresh_page()
        updated_count = int(order_feed_page.get_all_completed_orders_amount())

        assert all_completed_orders_amount + 1 == updated_count

    @allure.title('Счётчик выполненных сегодня заказов увеличивается после создания заказа')
    def test_today_orders_counter_increases_after_order_creation(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_order_feed_page()
        today_completed_orders_amount = int(order_feed_page.get_today_completed_orders_amount())

        auth_response = requests.post(f'{config.Urls.BASE_URL}{config.Urls.LOGIN_API_PATH}',
                                      json=data.LoginData.registered_user)
        access_token = auth_response.json().get('accessToken')
        auth_response.json().get('refreshToken')
        requests.post(f'{config.Urls.BASE_URL}{config.Urls.CREATE_ORDER_API_PATH}',
                      json=data.CreateOrderData.create_order_data, headers={
                'Authorization': access_token
            })
        order_feed_page.refresh_page()
        updated_count = int(order_feed_page.get_today_completed_orders_amount())

        assert today_completed_orders_amount + 1 == updated_count

    @allure.title('Номер созданного заказа отображается в блоке "В работе"')
    def test_order_number_is_presented_in_in_progress_status(self, driver, login_and_create_order):
        order_feed_page = OrderFeedPage(driver)
        order_number = login_and_create_order
        print(order_number)

        order_feed_page.open_order_feed_page()
        time.sleep(4)
        in_progress_orders = order_feed_page.get_in_progress_orders()

        assert str(order_number) in str(in_progress_orders)
