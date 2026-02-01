from logic.api_auth import AuthLogic
from logic.api_ingredients import IngredientsLogic
from helpers.generator import FakeUserGenerator
import pytest
import requests
import os


@pytest.fixture(scope="function")
def create_user():
    test_body = FakeUserGenerator().generate_user_body()
    logic_auth = AuthLogic()
    logic_auth.create_user(test_body, 200)
    return test_body

@pytest.fixture(scope="function")
def ingredients_list():
    logic_ingredients = IngredientsLogic()
    ingredients = logic_ingredients.get_ingredients(200)
    ingredients_list = [ingredients["data"][0]["_id"], ingredients["data"][1]["_id"]]
    return ingredients_list