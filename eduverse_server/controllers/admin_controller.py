import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.user import User  # noqa: E501
from eduverse_server import util


def get_users(role=None, page=None, limit=None):  # noqa: E501
    """Управление пользователями

     # noqa: E501

    :param role: Фильтр по роли
    :type role: str
    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[List[User], Tuple[List[User], int], Tuple[List[User], int, Dict[str, str]]
    """
    return 'do some magic!'
