# coding=utf-8

from flask import Blueprint, jsonify

bp_api_v1 = Blueprint('bp_api_v1', __name__, url_prefix='/api/v1')


@bp_api_v1.route('/')
def healthy_check():
    return jsonify(dict(foo='bar'))
