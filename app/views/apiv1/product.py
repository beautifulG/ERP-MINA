# coding=utf-8

from flask_restful import (
    Resource,
    reqparse,
    marshal_with_field,
    marshal_with,
    marshal,
)

from app.models import db, Product
from .validations import (
    exist_category,
    unique_product_name,
    unique_product_barcode,
)
from .fields import (
    product_fields,
    product_list_fields,
)


class ProductList(Resource):
    @marshal_with_field(product_list_fields)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=1)
        parser.add_argument('size', type=int, default=10)
        args = parser.parse_args()

        pagination = Product.query \
            .order_by(Product.inventory.desc()) \
            .paginate(args['page'], args['size'], error_out=False)
        return pagination.items

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=unique_product_name, required=True, trim=True)
        parser.add_argument('category', type=exist_category, required=True)
        parser.add_argument('barcode', type=unique_product_barcode, trim=True)
        parser.add_argument('description', type=str, default='', trim=True)
        parser.add_argument('inventory', type=int, default=0)
        args = parser.parse_args()

        product = Product(**args)
        db.session.add(product)
        db.session.commit()
        return marshal(product, product_fields), 201


class ProductItem(Resource):
    @marshal_with(product_fields)
    def get(self, id):
        product = Product.query.get_or_404(id)
        return product

    @marshal_with(product_fields)
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=unique_product_name, trim=True)
        parser.add_argument('category', type=exist_category)
        parser.add_argument('barcode', type=unique_product_barcode, trim=True)
        parser.add_argument('description', type=str, trim=True)
        args = parser.parse_args()

        product = Product.query.get_or_404(id)

        if args['name'] is not None:
            product.name = args['name']
        if args['category'] is not None:
            product.category = args['category']
        if args['barcode'] is not None:
            product.barcode = args['barcode']
        if args['description'] is not None:
            product.description = args['description']

        db.session.commit()

        return product
