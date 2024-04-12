from app.repositories.base_manager import BaseManager
from app.repositories.beverage_manager import BeverageManager
from app.repositories.index_manager import IndexManager
from app.repositories.ingredient_manager import IngredientManager
from app.repositories.order_manager import OrderManager
from app.repositories.size_manager import SizeManager
class ManagerFactory:
    _managers = {
        'base': BaseManager,
        'beverage': BeverageManager,
        'ingredient': IngredientManager,
        'size': SizeManager,
        'order': OrderManager,
        'index': IndexManager,
    }

    @classmethod
    def create_manager(cls, manager_name: str):
        if manager_name not in cls._managers:
            raise ValueError(f"Invalid manager name: '{manager_name}'")
        
        manager_class = cls._managers[manager_name]
        return manager_class()