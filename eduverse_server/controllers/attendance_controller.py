import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from eduverse_server.models.attendance_body import AttendanceBody  # noqa: E501
from eduverse_server.models.attendance_record import AttendanceRecord  # noqa: E501
from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server import util


def create_attendance(body):  # noqa: E501
    """Выставление посещаемости

    Доступно преподавателю и старосте # noqa: E501

    :param attendance_body: 
    :type attendance_body: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    attendance_body = body
    if connexion.request.is_json:
        attendance_body = AttendanceBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_attendance(student_id, page=None, limit=None):  # noqa: E501
    """Посещаемость студента

     # noqa: E501

    :param student_id: Идентификатор студента
    :type student_id: str
    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[List[AttendanceRecord], Tuple[List[AttendanceRecord], int], Tuple[List[AttendanceRecord], int, Dict[str, str]]
    """
    return 'do some magic!'
