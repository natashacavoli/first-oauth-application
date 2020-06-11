"""."""
from Model.client import Client


class Credential():
    """."""

    def __init__(self, client_id=None, client_secret=None):
        """."""
        self._client_id = client_id
        self._client_secret = client_secret

    @property
    def client_id(self):
        """."""
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        """."""
        self._client_id = value

    @property
    def client_secret(self):
        """."""
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value):
        """."""
        self._client_secret = value

    def authenticate(self):
        """."""
        if not self.client_id:

            return

        if not self.client_secret:

            return

        q = Client.query.filter_by(
            client_id=self.client_id,
            client_secret=self.client_secret).first()

        if q:

            return True

        return
