from allure import title
import pytest

from scheme.order_scheme import OrderScheme


class TestCreateOrder:

    @pytest.mark.parametrize('colour', [
        pytest.param(['BLACK']),
        pytest.param(['GREY']),
        pytest.param(["BLACK", "GREY"]),
        pytest.param(None)
    ])
    @title("Создание заказа")
    def test_create_order(self, colour):
        response_status_code, response_body = OrderScheme().create_order()
        assert response_status_code == 201 and response_body['track'] is not None

    @title("Получение списка заказов")
    def test_get_order_list(self):
        response_status_code, response_body = OrderScheme().check_order_list()
        assert response_status_code == 200 and response_body['orders'] is not None
