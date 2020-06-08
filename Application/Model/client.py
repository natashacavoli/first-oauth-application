"""."""
from .db import db
from sqlalchemy.dialects.postgresql import UUID


class Client(db.Model):
    """."""

    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(UUID(as_uuid=True))
    client_secret = db.Column(db.String(120))
    expires = db.Column(db.DateTime)

    def __init__(
            self,
            id=None,
            client_id=None,
            client_secret=None,
            expires=None):
        """."""
        self.id = id
        self.client_id = client_id
        self.client_secret = client_secret
        self.expires = expires
