import allure
import requests
from data import Urls, Components, ResponseMessages
from helpers import UserHelper

@allure.suite('Проверка процесса оформления заказа')
class TestOrderCreation:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_order_creation_authenticated_user(self, create_user):
        _, access_token = UserHelper.register_user()
        data = {'ingredients': [Components.BFLUORESCENT_BUN, Components.SAUCE_WITH_SPIKES]}
        order_creation = requests.post(Urls.ORDER_CREATION, data=data, headers={'Authorization': access_token})
        assert order_creation.json()['success'] is True

    @allure.title('Проверка создания заказа без авторизации')
    def test_order_creation_unauthenticated_user(self):
        data = {'ingredients': [Components.BFLUORESCENT_BUN, Components.SAUCE_WITH_SPIKES]}
        order_creation = requests.post(Urls.ORDER_CREATION, data=data)
        assert order_creation.json()['success'] is True

    @allure.title('Проверка создания заказа с некорректным хешем ингредиентов')
    def test_create_wrong_ingredient(self):
        data = {'ingredients': [Components.CRATER_BUN]}  # Некорректный компонент
        order_creation = requests.post(Urls.ORDER_CREATION, data=data)
        assert 500 == order_creation.status_code

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_without_ingredient(self):
        data = {'ingredients': ['']}  # Отсутствие компонентов
        order_creation = requests.post(Urls.ORDER_CREATION, data=data)
        assert 400 == order_creation.status_code and order_creation.json()['message'] == ResponseMessages.missing_ingredient