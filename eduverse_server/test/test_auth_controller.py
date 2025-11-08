import unittest

from flask import json

from eduverse_server.models.auth_login_body import AuthLoginBody  # noqa: E501
from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.inline_response200 import InlineResponse200  # noqa: E501
from eduverse_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_login(self):
        """Test case for login

        Вход в систему
        """
        auth_login_body = eduverse_server.AuthLoginBody()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/auth/login',
            method='POST',
            headers=headers,
            data=json.dumps(auth_login_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
