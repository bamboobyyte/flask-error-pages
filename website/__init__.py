from flask import Flask
from os import path

def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello world'

    from .pages import pages

    app.register_blueprint(pages, url_pregix='/')

    return app