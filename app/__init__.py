# coding=utf-8

from flask import Flask

from .views import init_app as views_init_app
from .models import db


def create_app(config_obj):
    """factory function"""
    app = Flask(__name__)
    app.config.from_object(config_obj)

    db.init_app(app)
    views_init_app(app)

    return app
