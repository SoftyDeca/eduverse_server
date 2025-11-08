import unittest

from flask import json

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from eduverse_server.models.transaction import Transaction  # noqa: E501
from eduverse_server.test import BaseTestCase


class TestCurrencyController(BaseTestCase):
    """CurrencyController integration test stubs"""

    def test_get_balance(self):
        """Test case for get_balance

        Баланс пользователя
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/currency/balance',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_transations(self):
        """Test case for get_transations

        История транзакций
        """
        query_string = [('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/currency/transactions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
