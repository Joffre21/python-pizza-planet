import pytest

def test_get_ingredient_report(create_ingredient_report):
    report = create_ingredient_report.json
    pytest.assume(create_ingredient_report.status.startswith('200'))
    for key in dict.keys():
        pytest.assume(report[key])

def test_get_month_report(create_month_report):
    report = create_month_report.json
    pytest.assume(create_month_report.status.startswith('200'))
    for key in dict.keys():
        pytest.assume(report[key])

def test_get_client_report(create_client_report):
    report = create_client_report.json
    pytest.assume(create_client_report.status.startswith('200'))
    for key in dict.keys():
        pytest.assume(report[key])