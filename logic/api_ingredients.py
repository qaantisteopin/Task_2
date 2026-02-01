from clients.ingredients import ClientIngredients
import allure

class IngredientsLogic:
    def get_ingredients(self, code):
        with allure.step(f"Получим список ингредиентов"):
            client = ClientIngredients()
            response = client.get_ingredients()
            assert response.status_code == code, f"Код ответа не равен {code}"
            return response.json()