from flask import Blueprint
from flask_restful import Api

API_BP = Blueprint('api_bp', __name__)
API = Api(API_BP)

# Import each API endpoint here
from pynashapi.api.moment import MOMENTS_HOLDER  # noqa
