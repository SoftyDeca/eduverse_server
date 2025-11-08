import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from eduverse_server.models.error import Error  # noqa: E501
from eduverse_server.models.product import Product  # noqa: E501
from eduverse_server import util


def create_product(body):  # noqa: E501
    """Добавить товар

     # noqa: E501

    :param product: 
    :type product: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    product = body
    if connexion.request.is_json:
        product = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_product_id(product_id):  # noqa: E501
    """Удалить продукт

    Удаление продукта по идентификатору. # noqa: E501

    :param product_id: 
    :type product_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_list_products(category=None, page=None, limit=None):  # noqa: E501
    """Список товаров

     # noqa: E501

    :param category: Фильтр по категории
    :type category: str
    :param page: Номер страницы
    :type page: int
    :param limit: Количество элементов на странице
    :type limit: int

    :rtype: Union[List[Product], Tuple[List[Product], int], Tuple[List[Product], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_product_id(product_id):  # noqa: E501
    """Получить продукт по ID

     # noqa: E501

    :param product_id: 
    :type product_id: str

    :rtype: Union[Product, Tuple[Product, int], Tuple[Product, int, Dict[str, str]]
    """
    return 'do some magic!'
