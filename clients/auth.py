import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ClientAuth:

    @staticmethod
    def create_user(body):
        url_suffix = os.getenv('AUTOTEST_URL_AUTH') + 'register'
        return requests.post(url=url_suffix, json=body)
    
    @staticmethod
    def login_user(body):
        url_suffix = os.getenv('AUTOTEST_URL_AUTH') + 'login'
        return requests.post(url=url_suffix, json=body)
    
    @staticmethod
    def delete_user(headers):
        url_suffix = os.getenv('AUTOTEST_URL_AUTH') + 'user'
        return requests.delete(url = url_suffix, headers=headers)
    
    @staticmethod
    def patch_user(headers):
        url_suffix = os.getenv('AUTOTEST_URL_AUTH') + 'user'
        return requests.patch(url = url_suffix, headers=headers)