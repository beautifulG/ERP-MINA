#!/usr/bin/env python3
# coding=utf-8

import os

from app import create_app
from config import config

app = create_app(config[os.getenv('FLASK_ENV') or 'default'])
