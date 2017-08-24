from flask import abort, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from pynashapi import DB
from pynashapi.api import API
from pynashapi.schemas.moment import MomentSchema
from pynashapi.libs.base_resource import BaseResource
from pynashapi.models import Moment


class Moments(BaseResource):
    def get(self):
        moments = Moment.query.order_by(Moment.event_date).all()

        if not moments:
            abort(404)
        return MomentSchema().dump(moments, many=True).data

    def post(self):
        request_json = request.get_json(force=True)
        moment_details = request_json['data']['attributes']
        try:
            validation_errors = MomentSchema().validate(request_json)
            if validation_errors:
                raise ValidationError(validation_errors)

            mmt = Moment(**moment_details)
            mmt.add()
            results = MomentSchema().dump(mmt).data
            return results, 201

        except ValidationError as err:
            resp = jsonify(err.messages)
            resp.status_code = 403
            return resp

        except SQLAlchemyError as e:
            DB.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 403
            return resp


API.add_resource(Moments, '/moments/')

# Used to enable Python to pull in the API resources
MOMENTS_HOLDER = None
