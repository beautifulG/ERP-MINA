# coding=utf-8

from flask_restful import fields

category_fields = {
    'id': fields.Integer,
    'name': fields.String,
}

product_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'inventory': fields.Integer,
    'barcode': fields.String,
    'category': fields.Nested(category_fields),
    'description': fields.String,
}

product_list_fields = fields.List(fields.Nested(product_fields))
