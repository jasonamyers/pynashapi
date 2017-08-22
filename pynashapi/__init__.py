from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from pynashapi.config import config

DB = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    DB.init_app(app)

    @app.route('/health/')
    def health_check():
        return jsonify({'health': 'OK'})

    return app
