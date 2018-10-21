# coding=utf-8

from flask import Blueprint
from flask_restful import Api

from .product import ProductList, ProductItem

bp_api_v1 = Blueprint('bp_api_v1', __name__, url_prefix='/api/v1')
api_v1 = Api(bp_api_v1)

api_v1.add_resource(ProductList, '/products')
api_v1.add_resource(ProductItem, '/products/<int:id>')
