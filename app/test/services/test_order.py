import pytest

from app.test.utils.functions import get_random_string, get_random_price

def test_create_order_service(create_orders):
    for order in create_orders:
        order_data = order.json
        pytest.assume(order.status.startswith('200'))
        pytest.assume(order_data['_id'])
        pytest.assume(order_data['client_name'])
        pytest.assume(order_data['client_dni'])
        pytest.assume(order_data['client_address'])
        pytest.assume(order_data['client_phone'])
        pytest.assume(order_data['date'])
        pytest.assume(order_data['total_price'])
        pytest.assume(order_data['size'])
        pytest.assume(order_data['detail'])

def test_get_order_by_id_service(client, create_orders, order_uri):
    for order in create_orders:
        current_order = order.json
        response = client.get(f'{order_uri}id/{current_order["_id"]}')
        pytest.assume(response.status.startswith('200'))
        returned_order = response.json
        for param, value in current_order.items():
            pytest.assume(returned_order[param] == value)


def test_get_order_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(order.json['_id'] in returned_orders)