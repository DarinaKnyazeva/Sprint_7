from allure import title

import helpers
from scheme.courier_scheme import CourierScheme


class TestCreateCourier:

    @title("Успешное создание курьера")
    def test_create_courier(self):
        data = helpers.register_new_courier_and_return_login_password()
        response_status_code, response_body = CourierScheme().create_courier(data)
        assert response_status_code == 201 and response_body == {'ok': True}

        login_response_status_code, login_response_body = CourierScheme().login_courier(data)
        delete_courier = CourierScheme().delete_courier(login_response_body['id'])
        assert delete_courier.status_code == 200

    @title("Cоздание курьера с повторяющимся логином")
    def test_create_courier_with_repeated_login(self):
        data = helpers.register_new_courier_and_return_login_password()
        response_status_code, response_body = CourierScheme().create_courier_with_repeated_login(data)
        assert response_status_code == 409 and response_body[
            'message'] == 'Этот логин уже используется. Попробуйте другой.'

        login_response_status_code, login_response_body = CourierScheme().login_courier(data)
        delete_courier = CourierScheme().delete_courier(login_response_body['id'])
        assert delete_courier.status_code == 200

    @title("Создание курьера без обязательных полей")
    def test_create_courier_without_required_field(self):
        data = helpers.register_new_courier_and_return_login_password()
        data_with_only_login = {'login': data['login']}
        response_status_code, response_body = CourierScheme().create_courier(data_with_only_login)
        assert response_status_code == 400 and response_body[
            'message'] == 'Недостаточно данных для создания учетной записи'

        login_response_status_code, login_response_body = CourierScheme().login_courier(data)
        delete_courier = CourierScheme().delete_courier(login_response_body['id'])
        assert delete_courier.status_code == 200
