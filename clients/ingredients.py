import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ClientIngredients:

    @staticmethod
    def get_ingredients():
        return requests.get(os.getenv('AUTOTEST_URL_INGREDIENTS'))