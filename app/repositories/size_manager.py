from app.repositories.base_manager import BaseManager
from app.repositories.models import Size
from app.repositories.serializers import SizeSerializer


class SizeManager(BaseManager):
    model = Size
    serializer = SizeSerializer