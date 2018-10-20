# coding=utf-8

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    products = db.relationship('Product', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.name


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False, default='')
    inventory = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Product %r>' % self.name


class StockIn(db.Model):
    __tablename__ = 'stockin'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<StockIn %r>' % self.id


class StockInDetail(db.Model):
    __tablename__ = 'stockin_detail'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    stockin_id = db.Column(db.Integer, db.ForeignKey(StockIn.id), nullable=False)
    amount = db.Column(db.Integer, nullable=False)


class StockOut(db.Model):
    __tablename__ = 'stockout'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    express = db.Column(db.String(32), nullable=False, default='')

    def __repr__(self):
        return '<StockOut %r>' % self.id


class StockOutDetail(db.Model):
    __tablename__ = 'stockout_detail'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)
    stockin_id = db.Column(db.Integer, db.ForeignKey(StockOut.id), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
