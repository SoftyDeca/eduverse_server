import unittest

from flask import json

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from eduverse_server.test import BaseTestCase


class TestScheduleController(BaseTestCase):
    """ScheduleController integration test stubs"""

    def test_get_schedule(self):
        """Test case for get_schedule

        Расписание занятий
        """
        query_string = [('date', '2025-10-25'),
                        ('page', 1),
                        ('limit', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/comand_5/API_EduVerse/1.0.0/schedule',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
