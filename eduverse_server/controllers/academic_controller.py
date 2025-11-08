import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.grade import Grade  # noqa: E501
from eduverse_server.models.homework import Homework  # noqa: E501
from eduverse_server.models.subject import Subject  # noqa: E501
from eduverse_server import util


def create_grade(body):  # noqa: E501
    """Добавить оценку

    Доступно только преподавателю # noqa: E501

    :param grade: 
    :type grade: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    grade = body
    if connexion.request.is_json:
        grade = Grade.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_homework(body):  # noqa: E501
    """Добавить домашнее задание

    Доступно преподавателю # noqa: E501

    :param homework: 
    :type homework: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    homework = body
    if connexion.request.is_json:
        homework = Homework.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_subject(body):  # noqa: E501
    """Добавить предмет

     # noqa: E501

    :param subject: 
    :type subject: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    subject = body
    if connexion.request.is_json:
        subject = Subject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_list_grades(student_id, page=None, limit=None):  # noqa: E501
    """Оценки студента

    Получение списка оценок конкретного студента # noqa: E501

    :param student_id: Идентификатор студента
    :type student_id: str
    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[List[Grade], Tuple[List[Grade], int], Tuple[List[Grade], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_list_homework(subject_id, page=None, limit=None):  # noqa: E501
    """Список домашнего задания

     # noqa: E501

    :param subject_id: 
    :type subject_id: str
    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[List[Homework], Tuple[List[Homework], int], Tuple[List[Homework], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_list_subject(page=None, limit=None):  # noqa: E501
    """Список предметов

     # noqa: E501

    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[List[Subject], Tuple[List[Subject], int], Tuple[List[Subject], int, Dict[str, str]]
    """
    return 'do some magic!'
