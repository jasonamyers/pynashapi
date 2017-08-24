from pynashapi import DB
from pynashapi.models.basemodel import ModelBase


class Moment(DB.Model, ModelBase):
    __tablename__ = 'moments'

    event_date = DB.Column(DB.Date, nullable=False)
    details = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return f'Moment(date={self.event_date}, details={self.details})'

    def __str__(self):
        return f'<moment: {self.event_date} - {self.details}>'
