# coding=utf-8

from app.models import Category, Product


def exist_category(value):
    """验证 category 存在"""
    category = Category.query.get(value)
    if not category:
        raise ValueError(f'分组 {value} 不存在')
    return category


def unique_product_name(value):
    """验证 product.name 唯一"""
    value = str(value)
    product = Product.query.filter_by(name=value).first()
    if product:
        raise ValueError(f'产品名称 {value} 重复')
    return value


def unique_product_barcode(value):
    """验证 product.barcode 唯一"""
    value = str(value)
    product = Product.query.filter_by(barcode=value).first()
    if product:
        raise ValueError(f'产品条形码 {value} 重复')
    return value
