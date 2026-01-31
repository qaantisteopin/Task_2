import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ClientAuth:

    @staticmethod
    def create_user(body):
        url_suffix = os.getenv('AUTOTEST_URL_AUTH') + 'register'
        return requests.post(url=url_suffix, json=body)