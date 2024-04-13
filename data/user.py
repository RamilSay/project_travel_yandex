import os
from dotenv import load_dotenv

load_dotenv()


class User:
    """
    User or test_user
    """

    def __init__(self, email: str, password: str, selenoid_login: str, selenoid_password: str, token: str = None):
        self.email = os.getenv('EMAIL') if email else 'test'
        self.password = os.getenv('PASSWORD') if password else 'test'
        self.selenoid_login = os.getenv('SELENOID_LOGIN')
        self.selenoid_password = os.getenv('SELENOID_PASSWORD')

    def selenoid_auth(self, selenoid_login, selenoid_password):
        return self
