import os
from dotenv import load_dotenv

load_dotenv()


class User:
    """
    User or test_user
    """

    def __init__(self, email: str, password: str, token: str = None):
        self.first_name = os.getenv('NAME')
        self.email = os.getenv('EMAIL') if email else 'test'
        self.password = os.getenv('PASSWORD') if password else 'test'
        self.token = ''
