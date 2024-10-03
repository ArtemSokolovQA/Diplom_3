import allure
import config
import locators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open_page(config.Urls.BASE_URL)

    @allure.step('Нажать на кнопку конструктор')
    def click_constructor_button(self):
        constructor_button = self.wait_and_find_element(locators.MainPageLocators.CONSTRUCTOR_BUTTON_LOCATOR)
        constructor_button.click()

    @allure.step('Нажать на кнопку лента заказов')
    def click_feed_button(self):
        feed_button = self.wait_and_find_element(locators.MainPageLocators.FEED_BUTTON_LOCATOR)
        feed_button.click()

    @allure.step('Кликнуть по карточке ингредиента')
    def click_ingredients_card(self):
        ingredients_card = self.wait_and_find_element(locators.MainPageLocators.INGREDIENT_CARD_BUTTON_LOCATOR)
        ingredients_card.click()

    @allure.step('Проверить, что открылось модальное окно деталей об ингредиенте')
    def check_ingredient_details_modal_appeared(self):
        ingredient_details_modal = self.wait_and_find_element(locators.MainPageLocators.INGREDIENT_DETAILS_MODAL_LOCATOR)
        return ingredient_details_modal

    @allure.step('Нажать на кнопку закрытия модального окна деталей ингредиента')
    def click_close_ingredient_modal_button(self):
        close_ingredient_modal_button = self.wait_and_find_element(locators.MainPageLocators.CLOSE_INGREDIENT_DETAILS_MODAL_BUTTON_LOCATOR)
        close_ingredient_modal_button.click()

    @allure.step('Проверить, что модальное окно закрылось')
    def check_ingredient_modal_is_closed(self):
        ingredient_modal = self.wait_and_find_element(locators.MainPageLocators.CLOSED_INGREDIENT_MODAL_LOCATOR)
        return ingredient_modal

    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(locators.MainPageLocators.INGREDIENT_CARD_BUTTON_LOCATOR, locators.MainPageLocators.BURGER_CONSTRUCTOR_BASKET_LOCATOR)