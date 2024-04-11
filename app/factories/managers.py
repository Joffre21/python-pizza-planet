from app.repositories.managers import BaseManager, BeverageManager, IndexManager, IngredientManager, OrderManager, SizeManager

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