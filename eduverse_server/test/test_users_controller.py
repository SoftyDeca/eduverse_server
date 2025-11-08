import unittest

from flask import json

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from eduverse_server.models.user import User  # noqa: E501
from eduverse_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Создать пользователя
        """
        user = {"role":"student","user_id":"usr_1","last_name":"Иванов","first_name":"Иван","email":"ivan@example.com"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/users',
            method='POST',
            headers=headers,
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user_id(self):
        """Test case for delete_user_id

        Удалить пользователя
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/users/{user_id}'.format(user_id='user_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Список пользователей
        """
        query_string = [('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/users',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_id(self):
        """Test case for get_user_id

        Получить пользователя по ID
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/users/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user_id(self):
        """Test case for update_user_id

        Обновить пользователя
        """
        user = {"role":"student","user_id":"usr_1","last_name":"Иванов","first_name":"Иван","email":"ivan@example.com"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/users/{user_id}'.format(user_id='user_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
