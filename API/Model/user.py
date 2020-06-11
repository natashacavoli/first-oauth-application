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
