from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

secret = '996db80a-debc-4828-8506-7bb4815450e4'
database = "mysql://root@localhost/agen.db"


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f'{database}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = f'{secret}'

    db.init_app(app)

    from .view_page.views import view

    app.register_blueprint(view, url_prefix='/')

    return app
