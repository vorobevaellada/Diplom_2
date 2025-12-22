import pytest
import allure
import requests
from data import Urls, ResponseMessages
from helpers import UserHelper

@allure.suite('Тестирование входа пользователя')
class TestAuthenticateUser:

    @allure.title('Проверка входа под существующим пользователем')
    def test_login_existing_user(self):
        user_data = UserHelper.authorized_user()
        response = requests.post(Urls.AUTHORIZATION, data=user_data)
        assert response.json()['success'] is True

    @allure.title('Проверка входа под несуществующим пользователем')
    @pytest.mark.parametrize('user_data', [
        UserHelper.invalid_credentials()['wrong_email'],
        UserHelper.invalid_credentials()['wrong_password']
    ])
    def test_authorization_user_with_invalid_data(self, user_data):
        response = requests.post(Urls.AUTHORIZATION, data=user_data)
        assert 401 == response.status_code and response.json()['message'] == ResponseMessages.unauthorized_user