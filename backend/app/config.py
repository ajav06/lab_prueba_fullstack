import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL')
        or 'postgresql://ash:dbpassword@localhost:5432/pokedex'
    )
    ENV = os.environ.get('ENV')
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'


class ProductionConfig(Config):
    ENV = 'PROD'
    pass


class DevelopmentConfig(Config):
    pass
