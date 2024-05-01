#!/usr/bin/python3
"""
used to register a blueprint app_views to one's flask api
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def teardown_appcontext(code):
    """teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ = '__main__':
    HOST = getenv('HBNB_API_HOST', 0.0.0.0)
    PORT(int(getenv('HBNB_API_PORT', 5000)))
    port=int(os.getenv('HBNB_API_PORT', '5000')))
