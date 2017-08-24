from functools import wraps

from flask import request
from flask_restful import abort
from flask_restful import Resource


def validate_content_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if (request.method == 'POST' and
                not request.headers.get('Content-Type') == 'application/json'):
            abort(415)
        return func(*args, **kwargs)

    return wrapper


class BaseResource(Resource):
    method_decorators = [validate_content_type]
