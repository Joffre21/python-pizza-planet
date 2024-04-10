from app.factories.managers import ManagerFactory
from .base import BaseController


class IngredientController(BaseController):
    manager = ManagerFactory.create_manager('ingredient')
