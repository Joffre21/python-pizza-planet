from app.common.http_methods import GET
from flask import Blueprint, jsonify

from ..controllers import IndexController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_index():
    return jsonify({"hola": "holaaa"})
