import pytest
import allure
import requests
from data import Urls, ResponseMessages
from helpers import UserHelper

@allure.suite('Тестирование создания пользователя')
class TestCreateUser:

    @allure.title('Проверка создания уникального пользователя')
    def test_create_unique_user(self):
        user_data = UserHelper.generate_valid_user()
        with allure.step("Регистрация пользователя"):
            response = requests.post(Urls.USER_REGISTRATION, data=user_data)
        assert response.status_code == 200 and response.json().get("accessToken")

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    def test_registered_user(self):
        user_data = UserHelper.authorized_user()
        with allure.step("Регистрация пользователя"):
            response = requests.post(Urls.USER_REGISTRATION, data=user_data)
        assert (403 == response.status_code and
                response.json().get('message') == ResponseMessages.registered_user)

    @allure.title('Проверка невозможности создания пользователя при отсутствии обязательных полей')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_user_creation_missing_fields(self, field):
        user_data = UserHelper.user_without_field(field)
        with allure.step("Регистрация пользователя"):
            response = requests.post(Urls.USER_REGISTRATION, data=user_data)
        assert (403 == response.status_code and
                response.json().get('message') == ResponseMessages.remove_blank_fields)