#!/usr/bin/python3
"""
used to register a blueprint app_views to one's flask api
"""
from flask import Blueprint

app_views = Blueprint('app_views',__name__, url_prefix='/api/v1')

from api.v1.views.index import *
