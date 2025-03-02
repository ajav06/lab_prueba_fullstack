from flask import Blueprint

sets = Blueprint("sets", __name__)

from . import views
