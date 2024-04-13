import pytest
from app.controllers import ReportController

def test_get_ingredient_report(app):
    ingredient_report, error = ReportController.get_ingredient_report()
    pytest.assume(error is None)
    for key, value in ingredient_report.items():
        pytest.assume(ingredient_report[key] == value)

def test_get_month_report(app):
    month_report, error = ReportController.get_month_report()
    pytest.assume(error is None)
    for key, value in month_report.items():
        pytest.assume(month_report[key] == value)

def test_get_client_report(app):
    client_report, error = ReportController.get_client_report()
    pytest.assume(error is None)
    for key, value in client_report.items():
        pytest.assume(client_report[key] == value)