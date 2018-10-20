#!/usr/bin/env python3
# coding=utf-8

from .apiv1 import bp_api_v1


def init_app(app):
    app.register_blueprint(bp_api_v1)
