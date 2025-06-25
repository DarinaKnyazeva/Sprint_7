from allure import title
import pytest

from scheme.order_scheme import OrderScheme


class TestCreateOrder:

    @title("Получение списка заказов")
    def test_get_order_list(self):
        response_status_code, response_body = OrderScheme().check_order_list()
        assert response_status_code == 200 and response_body['orders'] is not None
