from datetime import datetime

from pynashapi import DB


class ModelBase:
    id = DB.Column(DB.BigInteger, primary_key=True)
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow)
    updated_on = DB.Column(
        DB.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = DB.Column(DB.Boolean, default=True)

    def add(self):
        DB.session.add(self)
        return DB.session.commit()

    def update(self):
        return DB.session.commit()

    def delete(self):
        DB.session.delete(self)
        return DB.session.commit()
