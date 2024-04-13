from app.common.http_methods import GET, POST, PUT
from flask import Blueprint

from app.services import base_service

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)


@ingredient.route('/', methods=POST)
def create_ingredient():
    return base_service.create_item(IngredientController)


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return base_service.update_item(IngredientController)


@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
    return base_service.get_item_by_id(IngredientController, _id)


@ingredient.route('/', methods=GET)
def get_ingredients():
    return base_service.get_all_items(IngredientController)
