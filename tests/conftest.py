import pytest
import requests
from helpers import UserHelper
from data import Urls

@pytest.fixture
def create_user():
    user_data, access_token = UserHelper.register_user()
    yield user_data
    # Удаление пользователя с использованием полученного токена
    delete_user = requests.delete(Urls.CREATE_USER, headers={'Authorization': access_token})