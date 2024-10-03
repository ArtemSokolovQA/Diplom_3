from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_element(self, locator):
        self.wait_and_find_element(locator).click()

    def set_input(self, locator, value):
        element = self.wait_and_find_element(locator)
        element.clear()
        element.send_keys(value)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def check_element_disappeared_from_page(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located(locator))

    def set_access_token(self, access_token):
        self.driver.execute_script(f"window.localStorage.setItem('accessToken', '{access_token}');")

    def set_refresh_token(self, refresh_token):
        self.driver.execute_script(f"window.localStorage.setItem('refreshToken', '{refresh_token}');")

    def refresh_page(self):
        self.driver.refresh()

    def drag_and_drop_element(self, source_locator, target_locator):
        drag_and_drop(self.driver, source_locator, target_locator)