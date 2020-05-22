"""."""
import jwt


class Auth():
    """."""

    # Use RS256

    def __init__():
        """."""

    def _generate_access_token(self):
        """."""
        payload = {
            "issuer": "",
            "expiration": ""
        }

        # Create Issuer, Exp, Secret Key
        try:
            access_token = jwt.encode(
                payload, "", algorithm="HS256").decode()
        except:
            access_token = None

        return access_token

    def _verify_access_token(self, access_token):
        """."""
        try:
            access_token = access_token.encode()

            data = jwt.decode(
                access_token, "", algorithm=["HS256"])
        except:
            data = None

        return data
