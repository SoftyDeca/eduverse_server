import unittest

from flask import json

from eduverse_server.models.attendance_body import AttendanceBody  # noqa: E501
from eduverse_server.models.attendance_record import AttendanceRecord  # noqa: E501
from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.test import BaseTestCase


class TestAttendanceController(BaseTestCase):
    """AttendanceController integration test stubs"""

    def test_create_attendance(self):
        """Test case for create_attendance

        Выставление посещаемости
        """
        attendance_body = eduverse_server.AttendanceBody()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/attendance',
            method='POST',
            headers=headers,
            data=json.dumps(attendance_body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_attendance(self):
        """Test case for get_attendance

        Посещаемость студента
        """
        query_string = [('student_id', 'student_id_example'),
                        ('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/attendance',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
