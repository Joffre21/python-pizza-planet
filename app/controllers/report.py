from datetime import datetime
from app.factories.managers import ManagerFactory


class ReportController():
    beverage_manager = ManagerFactory.create_manager('beverage')
    size_manager = ManagerFactory.create_manager('size')
    order_manager = ManagerFactory.create_manager('order')
    ingredient_manager = ManagerFactory.create_manager('ingredient')

    @classmethod
    def get_ingredient_report(cls):
        ingredient_dict = cls.get_ingredient_dict()
        order_detail_list = cls.get_order_detail_list()
        ingredients_count = cls.get_count_ingredients(ingredient_dict, order_detail_list)
        return ingredients_count, None
    
    @classmethod
    def get_month_report(cls):
        month_dict = cls.get_month_dict()
        month_count = cls.get_count_money_by_month(month_dict)
        return month_count, None

    @classmethod
    def get_client_report(cls):
        client_dict = cls.get_client_dict()
        client_count = cls.get_count_money_by_client(client_dict)
        return client_count, None
    
    @staticmethod
    def get_ingredient_dict():
        ingredients = ReportController.ingredient_manager.get_all()
        ingredients_dict = {ingredient.get('name'): 0 for ingredient in ingredients}
        return ingredients_dict
    
    @staticmethod
    def get_order_detail_list():
        orders = ReportController.order_manager.get_all()
        order_detail_list = []
        for order in orders:
            for detail in order.get('detail'):
                if detail.get('ingredient') is  not None:
                    order_detail_list.append(detail.get('ingredient'))
        return order_detail_list
    
    @staticmethod
    def get_count_ingredients(ingredients_dict, order_detail_list):
        ingredients_count = ingredients_dict
        for ingredient in order_detail_list:
            if ingredient.get('name') in ingredients_dict:
                ingredients_count[ingredient.get('name')] = ingredients_count[ingredient.get('name')] + 1
        return ingredients_count
    
    @staticmethod
    def get_month_dict():
        orders = ReportController.order_manager.get_all()
        month_dict = {datetime.strptime(order.get('date'), '%Y-%m-%dT%H:%M:%S.%f').strftime('%B %Y'): 0 for order in orders}
        return month_dict
    
    @staticmethod
    def get_client_dict():
        orders = ReportController.order_manager.get_all()
        client_dict = {order.get('client_name'): 0 for order in orders}
        return client_dict
    
    @staticmethod
    def get_count_money_by_month(month_dict):
        response_dict = month_dict
        orders = ReportController.order_manager.get_all()
        for order in orders:
            date = datetime.strptime(order.get('date'), '%Y-%m-%dT%H:%M:%S.%f').strftime('%B %Y')
            if date in month_dict:
                response_dict[date] = response_dict[date] + order.get('total_price')
        return response_dict

    @staticmethod
    def get_count_money_by_client(client_dict):
        response_dict = client_dict
        orders = ReportController.order_manager.get_all()
        for order in orders:
            if order.get('client_name') in client_dict:
                response_dict[order.get('client_name')] = response_dict[order.get('client_name')] + order.get('total_price')
        return response_dict