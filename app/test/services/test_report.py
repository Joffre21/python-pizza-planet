import pytest

def test_get_ingredient_report(client, ingredient_report_uri):
    report = client.get(ingredient_report_uri)
    pytest.assume(report.status.startswith('308'))


def test_get_month_report(client, month_report_uri):
    report = client.get(month_report_uri)
    pytest.assume(report.status.startswith('308'))

def test_get_client_report(client, client_report_uri):
    report = client.get(client_report_uri)
    pytest.assume(report.status.startswith('308'))