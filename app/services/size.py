from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

from app.services import base_service

from ..controllers import SizeController

size = Blueprint('size', __name__)


@size.route('/', methods=POST)
def create_size():
    return base_service.create_item(SizeController)


@size.route('/', methods=PUT)
def update_size():
    return base_service.update_item(SizeController)

@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return base_service.get_item_by_id(SizeController, _id)

@size.route('/', methods=GET)
def get_sizes():
    return base_service.get_all_items(SizeController)