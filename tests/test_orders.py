import allure
import pytest
from logic.api_auth import AuthLogic
from logic.api_orders import OrdersLogic
from helpers.generator import FakeUserGenerator


@allure.epic("API Stellar")
@allure.feature("Orders")
class TestOrdersApi:

    @pytest.mark.parametrize("is_authorized, body, code", [(True, {
    "ingredients":["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]
}, 200),
                                            (True, None, 400),
                                            (True, {
    "ingredients":["61c0c5a71d1f82001bdaaa6m", "61c0c5a71d1f82001bdaaa6m"]
}, 500), (False, {
    "ingredients":["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]
}, 200), (False, None, 400), (False, {"ingredients":["61c0c5a71d1f82001bdaaa6m", "61c0c5a71d1f82001bdaaa6m"]}, 500)])
    @allure.story("Задание №4. Создание заказа")
    @allure.title("Создание заказа")
    def test_create_order(self, is_authorized, body, code):
        if is_authorized:
            test_body = FakeUserGenerator().generate_user_body()
            logic_auth = AuthLogic()
            logic_orders = OrdersLogic()
            logic_auth.create_user(test_body, 200)
            token = logic_auth.login_user(test_body, 200)["accessToken"]
            headers = {
                    "Authorization": token,
                    "Content-Type": "application/json" 
                        }
            result = logic_orders.create_order(headers, body, code)
            if code == 200:
                assert result["success"] == True
            elif code == 400:
                assert result["success"] == False
            logic_auth.delete_user(test_body, headers)
        else:
            logic_orders = OrdersLogic()
            result = logic_orders.create_order(None, body, code)
            if code == 200:
                assert result["success"] == True
            elif code == 400:
                assert result["success"] == False

    @pytest.mark.parametrize("is_authorized, code", [(True, 200),
                                                     (False, 401)])
    @allure.story(f"Задание №5. Получение заказа конкретного пользователя")
    @allure.title(f"Получение заказа конкретного пользователя")
    def test_get_orders(self, is_authorized, code):
        if is_authorized:
            test_body = FakeUserGenerator().generate_user_body()
            logic_auth = AuthLogic()
            logic_orders = OrdersLogic()
            logic_auth.create_user(test_body, 200)
            token = logic_auth.login_user(test_body, 200)["accessToken"]
            headers = {
                    "Authorization": token,
                    "Content-Type": "application/json" 
                        }
            result = logic_orders.get_order(headers, code)
            logic_auth.delete_user(test_body, headers)
            assert result["success"] == True

        else:
            logic_orders = OrdersLogic()
            result = logic_orders.get_order(None, code)
            assert result["success"] == False