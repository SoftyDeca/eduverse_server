import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from eduverse_server import util


def get_schedule(_date=None, page=None, limit=None):  # noqa: E501
    """Расписание занятий

    Берётся из базы данных # noqa: E501

    :param _date: Дата занятий (YYYY-MM-DD)
    :type _date: str
    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[List[InlineResponse2002], Tuple[List[InlineResponse2002], int], Tuple[List[InlineResponse2002], int, Dict[str, str]]
    """
    return 'do some magic!'
