from clients.orders import ClientOrders
import allure

class OrdersLogic:
    def create_order(self, headers, body, code):
        with allure.step(f"Создадим заказ"):
            client = ClientOrders()
            response = client.create_order(headers, body)
            assert response.status_code == code, f"Код ответа не равен {code}"
            if code != 500:
                return response.json()
            return response
        
    def get_order(self, headers, code):
        with allure.step(f"Получим заказ конкретного пользователя"):
            client = ClientOrders()
            response = client.get_order(headers)
            assert response.status_code == code, f"Код ответа не равен {code}"
            return response.json()