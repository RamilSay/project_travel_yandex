"""
import pytest
import allure
import json
from config import Config
from requests import Session
from curlify import to_curl
from allure_commons.types import AttachmentType


class BaseRequest(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, **kwargs):
        args = kwargs
        base_url = Config().base_url
        new_url = base_url + url
        method = method.upper()
        response = super().request(method=method, url=new_url, **kwargs)

        with allure.step(f'Отправляем запрос {method} {url} {args if len(args) != 0 else ""} '):
            message = to_curl(response.request)

            allure.attach(body=message.encode("utf8"), name="Curl", attachment_type=AttachmentType.TEXT,
                          extension='txt')
            allure.attach(body=json.dumps(response.json(), indent=4).encode("utf8"), name="Response Json",
                          attachment_type=AttachmentType.JSON, extension='json')

        return response


base_request = BaseRequest(Config.base_url)
"""