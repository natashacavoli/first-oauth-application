"""."""
from Model.client import Client
import jwt
import time


secret = ""


class Auth():
    """."""

    def __init__(self):
        """."""
        self.lifetime = 1800
        self.issuer = "simple-auth-api"

    def get_lifetime(self):
        """."""
        return self.lifetime

    def request_access_token(self, client_id, client_secret):
        """."""
        q = Client.query.filter_by(
            client_id=client_id,
            client_secret=client_secret).first()

        if q:

            return self.generate_access_token()

        return False

    def generate_access_token(self):
        """."""
        payload = {
            "iss": self.issuer,
            "exp": time.time() + self.lifetime,
            "client_id": ""
        }

        try:
            access_token = jwt.encode(
                payload, secret, algorithm="HS256").decode()
        except:
            access_token = None

        return access_token

    def verify_access_token(self, access_token):
        """."""
        try:
            access_token = access_token.encode()

            data = jwt.decode(
                access_token, secret, algorithm=["HS256"])
        except:
            data = None

        if data:

            try:
                if time.time() < data["exp"]:
                    return True
            except:
                return False

        return False
