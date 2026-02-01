import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ClientOrders:

    @staticmethod
    def create_order(headers, body):
        url_suffix = os.getenv('AUTOTEST_URL_ORDERS') 
        return requests.post(url=url_suffix,headers=headers, json=body)
    
    @staticmethod
    def get_order(headers):
        url_suffix = os.getenv('AUTOTEST_URL_ORDERS') 
        return requests.get(url=url_suffix,headers=headers)