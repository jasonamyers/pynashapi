from datetime import date

from flask_script import Command

from pynashapi.models import Moment


class DbInit(Command):
    """Creates database tables from sqlalchemy models
    """

    def __init__(self, db):
        self.db = db

    def run(self):
        self.db.create_all()


class DbProp(Command):
    """Propagate the Database
    """

    def __init__(self, db):
        self.db = db

    def run(self):
        prep_db(self.db)


def prep_db(db):
    m1 = Moment(
        id=1000,
        event_date=date(month=1, day=1, year=2017),
        details='Stuff happened')
    db.session.add(m1)
    db.session.commit()
