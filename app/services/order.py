from app.common.http_methods import GET, POST
from flask import Blueprint

from app.services import base_service

from ..controllers import OrderController

order = Blueprint('order', __name__)


@order.route('/', methods=POST)
def create_order():
    return base_service.create_item(OrderController)


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return base_service.get_item_by_id(OrderController, _id)


@order.route('/', methods=GET)
def get_orders():
    return base_service.get_all_items(OrderController)
