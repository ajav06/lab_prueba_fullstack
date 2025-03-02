import os

from flask import Flask

from app.config import Config, DevelopmentConfig, ProductionConfig
from app.db import db


def create_app():
    app = Flask(__name__)

    if os.environ.get("ENV", "").upper() == "LOCAL":
        app.config.from_object(Config())
    elif os.environ.get("ENV", "").upper() == "DEV":
        app.config.from_object(DevelopmentConfig())
    elif os.environ.get("ENV", "").upper() == "PROD":
        app.config.from_object(ProductionConfig())

    db.init_app(app)

    from .sets import sets

    app.register_blueprint(sets)

    return app
