from faker import Faker
import requests
from data import Urls

fake = Faker('ru_RU')  # глобально используем генератор фейковых данных

class UserHelper:

    @classmethod
    def generate_valid_user(cls):
        """Генерирует валидные данные пользователя"""
        return {
            'email': fake.email(),
            'password': fake.password(length=10),
            'name': fake.first_name()
        }

    @classmethod
    def generate_invalid_user(cls, field=''):
        """Создает пользователя с отсутствующим полем (field)"""
        user = cls.generate_valid_user()
        user[field] = ''  # очищаем заданное поле
        return user

    @classmethod
    def register_user(cls):
        """Регистрирует пользователя и возвращает его данные вместе с токеном"""
        user_data = cls.generate_valid_user()
        response = requests.post(Urls.USER_REGISTRATION, data=user_data)
        return user_data, response.json().get('accessToken')

    @classmethod
    def authorized_user(cls):
        """Возвращает зарегистрированного пользователя"""
        return {
            'email': 'milapro@ya.com',
            'password': 'milapro',
            'name': 'Artem'
        }

    @classmethod
    def invalid_credentials(cls):
        """Возвращает данные с неправильными учетными данными"""
        return {
            'wrong_email': {'email': 'invalid@example.com', 'password': '12345'},
            'wrong_password': {'email': 'valid@example.com', 'password': 'wrongpass'}
        }

    @classmethod
    def user_without_field(cls, field):
        """Создает пользователя без указанного поля (field)"""
        user = cls.generate_valid_user()
        del user[field]
        return user