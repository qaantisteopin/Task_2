import requests
import random
import string
import os 
from dotenv import load_dotenv

load_dotenv()


class FakeUserGenerator:
    def generate_random_string(self, length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
    
    
    def generate_user_body(self):
        login = self.generate_random_string(10) + "@yandex.ru"
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        body = {
            "email": login,
            "password": password,
            "name": first_name
        }

        return body
    
    def generate_order(self):
        first_name = self.generate_random_string(10)
        last_name = self.generate_random_string(10)
        address = f"{self.generate_random_string(5)}, apt. {random.randint(1, 200)}"
        metro_station = random.randint(1, 5)
        phone = f"+7 9{random.randint(00,99)}{random.randint(00,99)}{random.randint(00,99)}"
        rent_time = random.randint(1, 7)
        comment = self.generate_random_string(20)
        payload = {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": "2026-12-21",
        "comment": comment,
        "color": []
        }
        return payload