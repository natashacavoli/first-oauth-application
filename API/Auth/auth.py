"""."""
from .credential import Credential
import jwt
import time


secret = ""


class Auth():
    """."""

    def __init__(self,
                 lifetime=1800,
                 issuer="simple-auth-api"):
        """."""
        self._lifetime = lifetime
        self._issuer = issuer

    @property
    def lifetime(self):
        """."""
        return self._lifetime

    @lifetime.setter
    def lifetime(self, value):
        """."""
        self._lifetime = value

    @property
    def issuer(self):
        """."""
        return self._issuer

    @issuer.setter
    def issuer(self, value):
        """."""
        self._issuer = value

    def request_access_token(self, client_id, client_secret):
        """."""
        c = Credential()

        c.client_id = client_id
        c.client_secret = client_secret

        if c.authenticate():

            return self.encode_access_token(client_id)

        return False

    def validate_access_token(self, access_token):
        """."""
        data = self.decode_access_token(access_token)

        try:
            valid_keys = ["iss", "exp", "client_id"].sort()

            keys = list(data.keys()).sort()

            if valid_keys != keys:

                return False

            if time.time() > data.get("exp"):

                return False

            if self.issuer != data.get("iss"):

                return False

            return True
        except:
            return False

        return False

    def decode_access_token(self, access_token):
        """."""
        try:
            access_token = access_token.encode()

            data = jwt.decode(
                access_token, secret, algorithm=["HS256"])
        except:
            data = None

        return data

    def encode_access_token(self, client_id=""):
        """."""
        payload = {
            "iss": self.issuer,
            "exp": time.time() + self.lifetime,
            "client_id": client_id
        }

        try:
            access_token = jwt.encode(
                payload, secret, algorithm="HS256").decode()
        except:
            access_token = None

        return access_token
