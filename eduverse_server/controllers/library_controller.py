import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from eduverse_server.models.book import Book  # noqa: E501
from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.user import User  # noqa: E501
from eduverse_server import util


def create_book(body):  # noqa: E501
    """Добавить книгу

    Доступно преподавателю # noqa: E501

    :param book: 
    :type book: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    book = body
    if connexion.request.is_json:
        book = Book.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_book_id(book_id):  # noqa: E501
    """Удалить пользователя

    Удаление книги по её идентификатору. # noqa: E501

    :param book_id: 
    :type book_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_book_id(book_id):  # noqa: E501
    """Получить книгу по ID

     # noqa: E501

    :param book_id: 
    :type book_id: str

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_list_books(search=None, page=None, limit=None):  # noqa: E501
    """Список книг

     # noqa: E501

    :param search: Строка поиска по названию
    :type search: str
    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[List[Book], Tuple[List[Book], int], Tuple[List[Book], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_book_id(book_id, body):  # noqa: E501
    """Обновить книгу

     # noqa: E501

    :param book_id: 
    :type book_id: str
    :param user: 
    :type user: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    user = body
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
