from flask import jsonify, request

def get_retrieve_response(item, error):
    response = item if not error else { 'error': error }
    status_code = 200 if item else 404 if not error else 400
    return jsonify(response), status_code

def get_mutation_response(item, error):
    response = item if not error else { 'error': error }
    status_code = 200 if not error else 400
    return jsonify(response), status_code

def get_all_items(Controller):
    items, error = Controller.get_all()
    return get_retrieve_response(items, error)

def get_item_by_id(Controller, _id: int):
    item, error = Controller.get_by_id(_id)
    return get_retrieve_response(item, error)

def create_item(Controller):
    item, error = Controller.create(request.json)
    return get_mutation_response(item, error)

def update_item(Controller):
    item, error = Controller.update(request.json)
    return get_mutation_response(item, error)