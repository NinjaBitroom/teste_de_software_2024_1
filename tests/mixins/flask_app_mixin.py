import os

from flask import Flask

from src.services.database import db
from src.utils.setup import create_tables


class FlaskAppMixin:
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app = Flask(
            __name__,
            template_folder=os.path.abspath('templates'),
            static_folder=os.path.abspath('static')
        )
        app.config['SQLALCHEMY_DATABASE_URI'] = self.SQLALCHEMY_DATABASE_URI
        app.config['TESTING'] = self.TESTING
        app.secret_key = 'test'
        db.init_app(app)
        return app

    def setUp(self):
        create_tables(self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
