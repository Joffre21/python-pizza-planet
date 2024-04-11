from typing import Tuple
from sqlalchemy.exc import SQLAlchemyError

from app.factories.managers import ManagerFactory


class IndexController:

    @staticmethod
    def test_connection() -> Tuple[bool, str]:
        try:
            ManagerFactory.create_manager('index').test_connection()
            return True, ''
        except (SQLAlchemyError, RuntimeError) as ex:
            return False, str(ex)
