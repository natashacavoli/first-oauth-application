"""."""
from .db import db


class User(db.Model):
    """."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    email = db.Column(db.String(75))
    username = db.Column(db.String(75))
    password = db.Column(db.String(75))
    bio = db.Column(db.Text())

    def __init__(
            self,
            name=None,
            email=None,
            username=None,
            password=None,
            bio=None):
        """."""
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.bio = bio
