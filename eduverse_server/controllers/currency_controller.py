import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from eduverse_server.models.transaction import Transaction  # noqa: E501
from eduverse_server import util


def get_balance():  # noqa: E501
    """Баланс пользователя

     # noqa: E501


    :rtype: Union[InlineResponse2003, Tuple[InlineResponse2003, int], Tuple[InlineResponse2003, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_transations(page=None, limit=None):  # noqa: E501
    """История транзакций

     # noqa: E501

    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[List[Transaction], Tuple[List[Transaction], int], Tuple[List[Transaction], int, Dict[str, str]]
    """
    return 'do some magic!'
