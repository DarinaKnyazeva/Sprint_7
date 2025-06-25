import allure
import requests

from data import BASE_URL, COURIERS_URL, COURIERS_LOGIN_URL


class CourierScheme:

    @allure.step('Создание курьера')
    def create_courier(self, data):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data)
        return response.status_code, response.json()

    @allure.step('Удаление курьера')
    def delete_courier(self, id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}{id}')
        return response

    @allure.step('Создание курьера с повторяющимся логином')
    def create_courier_with_repeated_login(self, data):
        self.create_courier(data)
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data)
        return response.status_code, response.json()

    @allure.step('Авторизация курьера')
    def login_courier(self, data):
        self.create_courier(data)
        response = requests.post(f'{BASE_URL}{COURIERS_URL}{COURIERS_LOGIN_URL}', data, timeout=5)
        return response.status_code, response.json()

    @allure.step('Авторизация курьера с некорректными данными')
    def login_courier_with_wrong_data(self, data):
        self.create_courier(data)
        response = requests.post(f'{BASE_URL}{COURIERS_URL}{COURIERS_LOGIN_URL}',
                                 data={'login': '123', 'password': '123'})
        return response.status_code, response.json()
