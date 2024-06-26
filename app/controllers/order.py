from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

from app.factories.managers import ManagerFactory

from ..common.utils import check_required_keys
from .base import BaseController


class OrderController(BaseController):
    manager = ManagerFactory.create_manager('order')
    __required_info = ('client_name', 'client_dni', 'client_address', 'client_phone', 'size_id', 'date')

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list, beverages: list):
        price = sum(ingredient.price for ingredient in ingredients) + sum(beverage.price for beverage in beverages) + size_price
        return round(price, 2)

    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()
        if not current_order.get('date'):
            current_order.update({'date': datetime.now()})
            date = current_order.get('date')
        else: 
            stringDate = current_order.get('date')
            if stringDate.endswith('Z'):
                stringDate = stringDate[:-1]
            date = datetime.strptime(stringDate, '%Y-%m-%dT%H:%M:%S.%f')
        if not check_required_keys(cls.__required_info, current_order):
            return 'Invalid order payload', None

        size_id = current_order.get('size_id')
        size = ManagerFactory.create_manager('size').get_by_id(size_id)

        if not size:
            return 'Invalid size for Order', None

        ingredient_ids = current_order.pop('ingredients', [])
        beverages_ids = current_order.pop('beverages', [])
        try:
            ingredients = ManagerFactory.create_manager('ingredient').get_by_id_list(ingredient_ids)
            beverages = ManagerFactory.create_manager('beverage').get_by_id_list(beverages_ids)
            price = cls.calculate_order_price(size.get('price'), ingredients, beverages)
            order_with_price = {**current_order, 'total_price': price, 'date': date}
            return cls.manager.create(order_with_price, ingredients, beverages), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
