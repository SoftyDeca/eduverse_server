import unittest

from flask import json

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.user import User  # noqa: E501
from eduverse_server.test import BaseTestCase


class TestAdminController(BaseTestCase):
    """AdminController integration test stubs"""

    def test_get_users(self):
        """Test case for get_users

        Управление пользователями
        """
        query_string = [('role', 'role_example'),
                        ('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/admin/users',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
