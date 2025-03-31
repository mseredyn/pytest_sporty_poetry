import os

import allure
import requests


class BaseClient:
    def __init__(self):
        self.base_url = os.environ.get("BASE_API_URL")

    @allure.step
    def _get(self, endpoint:str, params=None, headers=None):
        return requests.get(f'{self.base_url}{endpoint}', params=params, headers=headers)