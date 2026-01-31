import allure
import pytest
import random
from src.logic.api_auth import AuthLogic
from src.helpers.generator import FakeUserGenerator


@allure.epic("API Яндекс.Самоката")
@allure.feature("Courier")
class TestCourierApi:

    @allure.story("Задание №1. Создание курьера")
    @allure.title("Создание курьера")
    def test_create_courier_with_valid_body_200(self):
        test_body = FakeUserGenerator().generate_body_json()
        logic_creation = CourierCreationLogic()
        logic_deletion = CourierDeletionLogic()
        logic_login = CourierLoginLogic()
        result = logic_creation.courier_creation(test_body, 201)
        assert result.json()["ok"] == True, "Тело ответа не соответствует контракту"
        del test_body["firstName"]
        id = logic_login.courier_login(test_body, 200)
        logic_deletion.courier_deletion(id)