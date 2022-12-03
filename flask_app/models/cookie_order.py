from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Cookies:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * from cookie_orders"
        results = connectToMySQL("cookie_orders_jg").query_db(query)
        cookies = []
        for x in results:
            cookies.append(cls(x))
        return cookies

    @classmethod
    def get_by_id(cls, order_id):
        query = "SELECT * from cookie_orders WHERE id = %(id)s;"
        data = {
            "id": order_id
        }
        result = connectToMySQL("cookie_orders_jg").query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def save_cookie(cls,data):
        query = "INSERT INTO cookie_orders (customer_name, cookie_type, num_boxes) VALUES (%(customer_name)s, %(cookie_type)s, %(num_boxes)s);"
        result = connectToMySQL("cookie_orders_jg").query_db(query, data)
        return result

    @classmethod
    def update(cls,data):
        query = "UPDATE cookie_orders SET customer_name = %(customer_name)s, cookie_type= %(cookie_type)s, num_boxes= %(num_boxes)s WHERE id = %(id)s;"
        result = connectToMySQL("cookie_orders_jg").query_db(query, data)
        return result
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM cookie_orders WHERE id = %(id)s;"
        result = connectToMySQL('cookie_orders_jg').query_db(query,data)
        return result


    @staticmethod
    def is_valid(user):
        is_valid = True
        if len(user["customer_name"]) <= 3:
            flash("Customer name must be longer than 3 characters!")
            is_valid = False
        if len(user["cookie_type"]) <= 3:
            flash("Customer name must be longer than 3 characters!")
            is_valid = False
        if len(user["num_boxes"]) <= 0:
            flash("Number of boxes must be greater than 0!")
            is_valid = False
        return is_valid
