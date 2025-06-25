import allure
import requests

import helpers
from data import BASE_URL, ORDERS_URL


class OrderScheme:

    @allure.step('Создание заказа')
    def create_order(self):
        data = helpers.register_new_order()
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', data=data)
        return response.status_code, response.json()

    @allure.step('Получение списка заказов')
    def check_order_list(self):
        helpers.register_new_order()
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.status_code, response.json()
