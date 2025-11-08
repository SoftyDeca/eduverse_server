import unittest

from flask import json

from eduverse_server.models.book import Book  # noqa: E501
from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.user import User  # noqa: E501
from eduverse_server.test import BaseTestCase


class TestLibraryController(BaseTestCase):
    """LibraryController integration test stubs"""

    def test_create_book(self):
        """Test case for create_book

        Добавить книгу
        """
        book = {"author":"А. Н. Иванов","book_id":"bk_1","title":"Основы программирования"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/library/books',
            method='POST',
            headers=headers,
            data=json.dumps(book),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_book_id(self):
        """Test case for delete_book_id

        Удалить пользователя
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/library/books/{book_id}'.format(book_id='book_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_book_id(self):
        """Test case for get_book_id

        Получить книгу по ID
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/library/books/{book_id}'.format(book_id='book_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_books(self):
        """Test case for get_list_books

        Список книг
        """
        query_string = [('search', 'search_example'),
                        ('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/library/books',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_book_id(self):
        """Test case for update_book_id

        Обновить книгу
        """
        user = {"role":"student","user_id":"usr_1","last_name":"Иванов","first_name":"Иван","email":"ivan@example.com"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/library/books/{book_id}'.format(book_id='book_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
