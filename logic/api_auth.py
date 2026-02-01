from clients.auth import ClientAuth
import allure

class AuthLogic:
    def create_user(self, body, code):
        with allure.step(f'Создадим пользователя с данными {body}'):
            client = ClientAuth()
            response = client.create_user(body)
            assert response.status_code == code, f"Код ответа не равен {code}"
            if response.status_code == 403:
                return response.json()
            return response
    
    def login_user(self, body, code):
        with allure.step(f"Залогинимся с данными {body}"):
            client = ClientAuth()
            response = client.login_user(body)
            assert response.status_code == code, f"Код ответа не равен {code}"
            return response.json()

    def delete_user(self, body, headers):
        with allure.step(f"Удалим пользователя с данными {body}"):
            client = ClientAuth()
            response = client.delete_user(headers)
            assert response.status_code == 202, f"Код ответа не равен 202"

    def patch_user(self, body, headers, code):
        with allure.step(f"Изменим пользователя на данные {body}"):
            client = ClientAuth()
            response = client.patch_user(headers)
            assert response.status_code == code, f"Код ответа не равен {code}"
            return response.json()