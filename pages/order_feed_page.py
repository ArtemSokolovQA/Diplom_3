import allure

import config
import data
import locators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step('Открыть страницу ленты заказов')
    def open_order_feed_page(self):
        self.open_page(f'{config.Urls.BASE_URL}{config.Urls.FEED_PATH}')

    @allure.step('Кликнуть по карточке заказа')
    def click_order_card(self):
        order_card = self.wait_and_find_element(locators.OrderFeedPageLocators.ORDER_CARD_LOCATOR)
        order_card.click()


    @allure.step('Проверить, что открылось модальное окно деталей о заказе')
    def check_order_details_modal_is_opened(self):
        order_details_modal = self.wait_and_find_element(locators.OrderFeedPageLocators.ORDER_DETAILS_MODAL_LOCATOR)
        return order_details_modal

    @allure.step('Проверить, что в карточке заказа есть номер заказа')
    def check_order_number_in_order_card(self):
        order_card = self.wait_and_find_element(locators.OrderFeedPageLocators.ORDER_DETAILS_MODAL_NUMBER_LOCATOR)
        return order_card.text

    @allure.step('Получить количество выполненных заказов за все время')
    def get_all_completed_orders_amount(self):
        all_completed_orders_counter = self.wait_and_find_element(locators.OrderFeedPageLocators.ALL_COMPLETED_ORDERS_COUNTER_LOCATOR)
        return all_completed_orders_counter.text

    @allure.step('Получить количество выполненных заказов за сегодняшний день')
    def get_today_completed_orders_amount(self):
        today_completed_orders_counter = self.wait_and_find_element(locators.OrderFeedPageLocators.TODAY_COMPLETED_ORDERS_COUNTER_LOCATOR)
        return today_completed_orders_counter.text

    @allure.step('Получить заказы, находящиеся в статусе "В работе"')
    def get_in_progress_orders(self):
        in_progress_orders = self.wait_and_find_element(locators.OrderFeedPageLocators.IN_PROGRESS_ORDERS_LOCATOR)
        return in_progress_orders.text
