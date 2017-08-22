import pytest

from pynashapi import create_app, DB


@pytest.fixture()
def testapp(request):
    app = create_app('testing')
    client = app.test_client()

    DB.app = app
    DB.create_all()

    def teardown():
        DB.session.remove()
        DB.drop_all()

    request.addfinalizer(teardown)

    return client
