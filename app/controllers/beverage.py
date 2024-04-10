from app.controllers.base import BaseController
from app.factories.managers import ManagerFactory


class BeverageController(BaseController):
    manager = ManagerFactory.create_manager('beverage')