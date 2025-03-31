import allure

from api.base_client import BaseClient


class PoetryClient(BaseClient):
    _AUTHOR = "/author"

    def __init__(self):
        super().__init__()

    @allure.step
    def get_author(self, author_name):
        return self._get(f'{self._AUTHOR}/{author_name}')

    @allure.step
    def get_authors(self):
        return self._get(self._AUTHOR)
