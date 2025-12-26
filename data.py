class Urls:
    MAIN_URL = 'https://stellarburgers.education-services.ru/'
    ORDER_CREATION = f"{MAIN_URL}/api/orders" # Создание заказа
    CREATE_USER = f"{MAIN_URL}/api/auth/user" # создание пользователя
    AUTHORIZATION = f"{MAIN_URL}/api/auth/login" # Авторизация
    USER_REGISTRATION = f"{MAIN_URL}/api/auth/register" # Регистрация пользователя

class Components:
    BFLUORESCENT_BUN = '61c0c5a71d1f82001bdaaa6d'
    CRATER_BUN = '61c0c3a2221d1f81101bdaaa6d'
    SAUCE_WITH_SPIKES = '61c0c5a71d1f82001bdaaa75'

class ResponseMessages:
    registered_user = 'User already exists' # Если пользователь существует
    remove_blank_fields = 'Email, password and name are required fields' # Если нет одного из полей
    unauthorized_user = 'email or password are incorrect' # Если логин или пароль НЕверные
    missing_ingredient = 'Ingredient ids must be provided'