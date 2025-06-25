from allure import title
import helpers
from scheme.courier_scheme import CourierScheme


class TestLoginCourier:

    @title("Успешная авторизация курьера")
    def test_login_courier(self):
        data = helpers.register_new_courier_and_return_login_password()
        response_status_code, response_body = CourierScheme().login_courier(data)
        assert response_status_code == 200 and response_body['id'] is not None

        login_response_status_code, login_response_body = CourierScheme().login_courier(data)
        delete_courier = CourierScheme().delete_courier(login_response_body['id'])
        assert delete_courier.status_code == 200

    @title("Авторизация курьера без обязательных полей")
    def test_login_courier_without_required_field(self):
        data = helpers.register_new_courier_and_return_login_password()
        data_with_only_login = {'login': data['login']}
        response_status_code, response_body = CourierScheme().login_courier(data_with_only_login)
        assert response_status_code == 400 and response_body['message'] == 'Недостаточно данных для входа'

        login_response_status_code, login_response_body = CourierScheme().login_courier(data)
        delete_courier = CourierScheme().delete_courier(login_response_body['id'])
        assert delete_courier.status_code == 200

    @title("Авторизация курьера с некорректными данными")
    def test_login_courier_with_wrong_data(self):
        data = helpers.register_new_courier_and_return_login_password()
        response_status_code, response_body = CourierScheme().login_courier_with_wrong_data(data)
        assert response_status_code == 404 and response_body['message'] == 'Учетная запись не найдена'

        login_response_status_code, login_response_body = CourierScheme().login_courier(data)
        delete_courier = CourierScheme().delete_courier(login_response_body['id'])
        assert delete_courier.status_code == 200
