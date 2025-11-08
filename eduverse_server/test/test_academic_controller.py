import unittest

from flask import json

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.grade import Grade  # noqa: E501
from eduverse_server.models.homework import Homework  # noqa: E501
from eduverse_server.models.subject import Subject  # noqa: E501
from eduverse_server.test import BaseTestCase


class TestAcademicController(BaseTestCase):
    """AcademicController integration test stubs"""

    def test_create_grade(self):
        """Test case for create_grade

        Добавить оценку
        """
        grade = {"subject_id":"sub_1","grade":5}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/academic/grades',
            method='POST',
            headers=headers,
            data=json.dumps(grade),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_homework(self):
        """Test case for create_homework

        Добавить домашнее задание
        """
        homework = {"subject_id":"subject_id","description":"description","title":"title","deadline":"2000-01-23"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/academic/homework',
            method='POST',
            headers=headers,
            data=json.dumps(homework),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_subject(self):
        """Test case for create_subject

        Добавить предмет
        """
        subject = {"subject_id":"sub_1","name":"Математика"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/academic/subjects',
            method='POST',
            headers=headers,
            data=json.dumps(subject),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_grades(self):
        """Test case for get_list_grades

        Оценки студента
        """
        query_string = [('student_id', 'student_id_example'),
                        ('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/academic/grades',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_homework(self):
        """Test case for get_list_homework

        Список домашнего задания
        """
        query_string = [('subject_id', 'subject_id_example'),
                        ('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/academic/homework',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_list_subject(self):
        """Test case for get_list_subject

        Список предметов
        """
        query_string = [('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/academic/subjects',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
