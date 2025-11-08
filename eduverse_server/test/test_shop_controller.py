import unittest

from flask import json

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.product import Product  # noqa: E501
from eduverse_server.test import BaseTestCase


class TestShopController(BaseTestCase):
    """ShopController integration test stubs"""

    def test_create_product(self):
        """Test case for create_product

        Добавить товар
        """
        product = {"price":250,"product_id":"prd_1","name":"Фон профиля — Космос","currency":"EDC"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/shop/products',
            method='POST',
            headers=headers,
            data=json.dumps(product),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_product_id(self):
        """Test case for delete_product_id

        Удалить продукт
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/shop/products/{product_id}'.format(product_id='product_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_products(self):
        """Test case for get_list_products

        Список товаров
        """
        query_string = [('category', 'category_example'),
                        ('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/shop/products',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_product_id(self):
        """Test case for get_product_id

        Получить продукт по ID
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/shop/products/{product_id}'.format(product_id='product_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
