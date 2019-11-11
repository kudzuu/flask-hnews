"""
Define the Story model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Story(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Story model """

    __tablename__ = "story"

    title = db.Column(db.String(300), primary_key=True)
    url = db.Column(db.String(300), primary_key=True)
    created_at = db.Column(db.Integer, nullable=False)

    def __init__(self, title, url, created_at=None):
        """ Create a new Story """
        self.title = title
        self.url = url
        self.created_at = created_at
