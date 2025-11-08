import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from eduverse_server.models.user import User  # noqa: E501
from eduverse_server import util


def create_user(body):  # noqa: E501
    """Создать пользователя

    Доступно только администратору # noqa: E501

    :param user: 
    :type user: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    user = body
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user_id(user_id):  # noqa: E501
    """Удалить пользователя

    Удаление пользователя по его идентификатору. Доступно только администратору # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user(page=None, limit=None):  # noqa: E501
    """Список пользователей

    Доступно только администратору # noqa: E501

    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[InlineResponse2001, Tuple[InlineResponse2001, int], Tuple[InlineResponse2001, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_id(user_id):  # noqa: E501
    """Получить пользователя по ID

    Доступно только администратору # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: Union[User, Tuple[User, int], Tuple[User, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_user_id(user_id, body):  # noqa: E501
    """Обновить пользователя

    Доступно только администратору # noqa: E501

    :param user_id: 
    :type user_id: str
    :param user: 
    :type user: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    user = body
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
