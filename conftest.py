import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import config
import data
import pytest


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def login():
    response = requests.post(f'{config.Urls.BASE_URL}{config.Urls.LOGIN_API_PATH}', json=data.LoginData.registered_user)

    access_token = response.json().get('accessToken')
    refresh_token = response.json().get('refreshToken')

    return access_token, refresh_token


@pytest.fixture
def login_and_create_order():
    auth_response = requests.post(f'{config.Urls.BASE_URL}{config.Urls.LOGIN_API_PATH}', json=data.LoginData.registered_user)

    access_token = auth_response.json().get('accessToken')
    refresh_token = auth_response.json().get('refreshToken')
    create_order_response = requests.post(f'{config.Urls.BASE_URL}{config.Urls.CREATE_ORDER_API_PATH}', json=data.CreateOrderData.create_order_data, headers={
        'Authorization': access_token
    })

    order_number = create_order_response.json()['order']['number']

    return order_number




