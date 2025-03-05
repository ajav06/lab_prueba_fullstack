import os

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

from app.config import Config, DevelopmentConfig, ProductionConfig
from app.db import db


def create_app():
    """
    Summary
    -------
    Initializes a Flask application with different configurations based on the environment
    variable and registers blueprints for sets and cards

    Returns
    -------
        Returning an instance of the Flask application after setting up the configuration
        based on the environment variable "ENV" and registering blueprints for sets and
        cards
    """
    app = Flask(__name__)

    if os.environ.get("ENV", "").upper() == "LOCAL":
        app.config.from_object(Config())
    elif os.environ.get("ENV", "").upper() == "DEV":
        app.config.from_object(DevelopmentConfig())
    elif os.environ.get("ENV", "").upper() == "PROD":
        app.config.from_object(ProductionConfig())

    db.init_app(app)

    swagger_ui_blueprint = get_swaggerui_blueprint(
        app.config['SWAGGER_URL'],
        app.config['API_URL'],
        config={'app_name': 'Access API'},
    )

    app.register_blueprint(swagger_ui_blueprint, url_prefix=app.config['SWAGGER_URL'])

    from .sets import sets

    app.register_blueprint(sets)

    from .cards import cards

    app.register_blueprint(cards)

    return app
