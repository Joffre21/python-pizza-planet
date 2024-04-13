from app.common.http_methods import GET
from flask import Blueprint

from app.controllers.report import ReportController
from app.services import base_service

report = Blueprint('report', __name__)


@report.route('/ingredient/', methods=GET)
def get_ingredient_report():
    return base_service.get_special_report(ReportController, 'ingredient')

@report.route('/month/', methods=GET)
def get_month_report():
    return base_service.get_special_report(ReportController, 'month')

@report.route('/client/', methods=GET)
def get_client_report():
    return base_service.get_special_report(ReportController, 'client')
