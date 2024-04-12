from typing import Sequence
from app.repositories.base_manager import BaseManager
from app.repositories.models import Beverage
from app.repositories.serializers import BeverageSerializer


class BeverageManager(BaseManager):
    model = Beverage
    serializer = BeverageSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []