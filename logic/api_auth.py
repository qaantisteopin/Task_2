from src.clients.auth import ClientAuth
import allure

class AuthLogic:
    def create_user(self, body, code):
        with allure.step(f'Создадим пользователя с данными {body}'):
            client = ClientAuth()
            response = client.create_user(body)
            assert response.status_code == code, f"Код ответа не равен {code}"
            if response.status_code == 403:
                return response.json()["id"]
            return response