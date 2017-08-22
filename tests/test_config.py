import os

from pynashapi import create_app

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def test_development_config():
    app = create_app('development')
    assert app.config['DEBUG']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + \
        os.path.join(basedir, 'data-dev.sqlite')


def test_testing_config():
    app = create_app('testing')
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + \
        os.path.join(basedir, 'data-test.sqlite')
