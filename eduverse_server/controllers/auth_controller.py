import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from eduverse_server.models.auth_login_body import AuthLoginBody  # noqa: E501
from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.inline_response200 import InlineResponse200  # noqa: E501
from eduverse_server import util


def login(body):  # noqa: E501
    """Вход в систему

    Авторизация по email и паролю # noqa: E501

    :param auth_login_body: 
    :type auth_login_body: dict | bytes

    :rtype: Union[InlineResponse200, Tuple[InlineResponse200, int], Tuple[InlineResponse200, int, Dict[str, str]]
    """
    auth_login_body = body
    if connexion.request.is_json:
        auth_login_body = AuthLoginBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
