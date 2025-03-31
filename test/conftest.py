import pytest

from api.poetry_client import PoetryClient


@pytest.fixture(scope="function")
def poetry_client():
    yield PoetryClient()
