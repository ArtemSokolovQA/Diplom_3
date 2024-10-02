from selenium.webdriver.common.by import By


class LoginPageLocators:
    RESTORE_PASSWORD_BUTTON_LOCATOR = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/forgot-password"]')


class RestorePasswordLocators:

    EMAIL_INPUT_LOCATOR = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"]')
    RESTORE_PASSWORD_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    RESTORE_PASSWORD_TITLE_LOCATOR = (By.XPATH, '//h2[text()="Восстановление пароля"]')
    NEW_PASSWORD_INPUT_LOCATOR = (By.XPATH, '//input[@class="text input__textfield text_type_main-default"][@type="password"]')
    SHOW_PASSWORD_BUTTON_LOCATOR = (By.XPATH, '//div[@class="input__icon input__icon-action"]//*[name()="svg"]')
    DEFAULT_PASSWORD_INPUT = (By.XPATH, '//label[@class="input__placeholder text noselect text_type_main-default" and text()="Пароль"]')
    FOCUSED_PASSWORD_INPUT = (By.XPATH, '//label[@class="input__placeholder text noselect text_type_main-default input__placeholder-focused" and text()="Пароль"]')


class PersonalCabinetLocators:

    HEADER_PERSONAL_CABINET_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/account"]')
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
    ORDER_HISTORY_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/account/order-history"]')
    LOGIN_TITLE_LOCATOR = (By.XPATH, '//h2[text()="Вход"]')


class MainPageLocators:

    FEED_BUTTON_LOCATOR = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and @href="/feed"]')
    CONSTRUCTOR_BUTTON_LOCATOR = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo" and @href="/"]')
    INGREDIENT_DETAILS_MODAL_LOCATOR = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]')
    INGREDIENT_CARD_BUTTON_LOCATOR = (By.XPATH, '//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"][1]')
    CLOSE_INGREDIENT_DETAILS_MODAL_BUTTON_LOCATOR = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"][1]')
    CLOSED_INGREDIENT_MODAL_LOCATOR = (By.XPATH, '//section[@class="Modal_modal__P3_V5"]')
    BURGER_CONSTRUCTOR_BASKET_LOCATOR = (By.XPATH, '//ul[@class="BurgerConstructor_basket__list__l9dp_"]')


class OrderFeedPageLocators:

    ORDER_CARD_LOCATOR = (By.XPATH, '//li[@class="OrderHistory_listItem__2x95r mb-6"][1]')
    ORDER_DETAILS_MODAL_LOCATOR = (By.XPATH, '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
    ORDER_DETAILS_MODAL_NUMBER_LOCATOR = (By.XPATH, '//p[@class="text text_type_digits-default"][1]')
    ALL_COMPLETED_ORDERS_COUNTER_LOCATOR = (By.XPATH, '(//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"])[1]')
    TODAY_COMPLETED_ORDERS_COUNTER_LOCATOR = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/div[3]/p[2]')
    IN_PROGRESS_ORDERS_LOCATOR = (By.XPATH, '//li[@class="text text_type_main-small"]')


