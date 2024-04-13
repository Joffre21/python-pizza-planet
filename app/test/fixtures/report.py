import pytest
import math

from ..utils.functions import get_random_string, get_random_price

def ingredient_report_mock() -> dict:
    return {
        get_random_string: math.floor(get_random_price(0, 10))
    }

def month_client_report_mock() -> dict:
    return {
        get_random_string: get_random_price(0, 20)
    }

@pytest.fixture()
def create_ingredient_report():
    return ingredient_report_mock()

@pytest.fixture
def create_month_report():
    return month_client_report_mock()

@pytest.fixture
def create_client_report():
    return month_client_report_mock()