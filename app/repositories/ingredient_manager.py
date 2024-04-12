from typing import Sequence
from app.repositories.base_manager import BaseManager
from app.repositories.models import Ingredient
from app.repositories.serializers import IngredientSerializer


class IngredientManager(BaseManager):
    model = Ingredient
    serializer = IngredientSerializer

    @classmethod
    def get_by_id_list(cls, ids: Sequence):
        return cls.session.query(cls.model).filter(cls.model._id.in_(set(ids))).all() or []