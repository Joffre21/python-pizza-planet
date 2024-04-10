from app.factories.managers import ManagerFactory
from .base import BaseController


class SizeController(BaseController):
    manager = ManagerFactory.create_manager('size')
