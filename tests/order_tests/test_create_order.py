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


