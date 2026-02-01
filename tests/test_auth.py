import allure
import copy
import pytest
from logic.api_auth import AuthLogic
from helpers.generator import FakeUserGenerator


@allure.epic("API Stellar")
@allure.feature("Auth")
class TestAuthApi:

    @allure.story("Задание №1. Создание пользователя")
    @allure.title("Создание пользователя")
    def test_create_user_with_valid_body_200(self):
        test_body = FakeUserGenerator().generate_user_body()
        logic_auth = AuthLogic()
        logic_auth.create_user(test_body, 200)
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        logic_auth.delete_user(test_body, headers)

    @pytest.mark.parametrize("test_body_key, code", [
                                                    ("email", 403),
                                                    ("password", 403),
                                                    ("name", 403)])
    @allure.story("Задание №1. Создание пользователя")
    @allure.title("Создание пользователя без одного из необходимых полей")
    def test_create_user_with_invalid_test_body_403(self, test_body_key, code):
        test_body = FakeUserGenerator().generate_user_body()
        del test_body[test_body_key]
        logic_auth = AuthLogic()
        result = logic_auth.create_user(test_body, code)
        assert result["success"] == False
        assert result["message"] == "Email, password and name are required fields"

    @allure.story("Задание №1. Создание пользователя")
    @allure.title("Создание существующего пользователя")
    def test_create_user_existed_403(self):
        test_body = FakeUserGenerator().generate_user_body()
        logic_auth = AuthLogic()
        logic_auth.create_user(test_body, 200)
        result = logic_auth.create_user(test_body, 403)
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        logic_auth.delete_user(test_body, headers)
        assert result["success"] == False
        assert result["message"] == "User already exists"

    @allure.story("Задание №2. Логин пользователя")
    @allure.title("Логин пользователя")
    def test_login_user_existed_200(self, create_user):
        test_body = create_user
        logic_auth = AuthLogic()
        result = logic_auth.login_user(test_body, 200)
        token = result["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        logic_auth.delete_user(test_body, headers)
        assert result["success"] == True

    @pytest.mark.parametrize("test_body_key, code", [("email", 401),
                                                     ("password", 401)])
    @allure.story("Задание №2. Логин пользователя")
    @allure.title("Логин пользователя c невалидными данными")
    def test_login_user_existed_200(self, create_user, test_body_key, code):
        test_body = create_user
        logic_auth = AuthLogic()
        test_body_copy = copy.deepcopy(test_body)
        del test_body_copy[test_body_key]
        test_result = logic_auth.login_user(test_body_copy, code)
        result = logic_auth.login_user(test_body, 200)
        token = result["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        logic_auth.delete_user(test_body, headers)
        assert test_result["success"] == False
        assert test_result["message"] == "email or password are incorrect"

    @pytest.mark.parametrize("test_body_key", [("email", ), ("password", ),("name", )])
    @allure.story("Задание №3. Изменение данных пользователя")
    @allure.title("Изменение данных пользователя")
    def test_patch_user_existed_200(self, create_user, test_body_key):
        test_body = create_user
        logic_auth = AuthLogic()
        result = logic_auth.login_user(test_body, 200)
        token = result["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        if test_body_key == "email":
            new_value = FakeUserGenerator().generate_random_string() + "@yandex.ru"
            test_body[test_body_key] = new_value
        else:
            new_value = FakeUserGenerator().generate_random_string()
            test_body[test_body_key] = new_value
        test_result = logic_auth.patch_user(test_body, headers, 200)
        logic_auth.delete_user(test_body, headers)
        assert test_result["success"] == True
        if test_body_key != "email":
            assert test_result["user"][test_body_key] == new_value

    @allure.story("Задание №3. Изменение данных пользователя")
    @allure.title("Изменение данных пользователя без авторизации")
    def test_patch_user_existed_200(self, create_user):
        test_body = create_user
        logic_auth = AuthLogic()
        result = logic_auth.login_user(test_body, 200)
        token = result["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        test_headers = None
        test_result = logic_auth.patch_user(test_body, test_headers, 401)
        logic_auth.delete_user(test_body, headers)
        assert test_result["success"] == False
        assert test_result["message"] == "You should be authorised"