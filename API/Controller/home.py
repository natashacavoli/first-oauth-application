"""."""
from flask import request, Blueprint
from Auth.auth import Auth

home_blueprint = Blueprint("home_blueprint", __name__)

auth = Auth()


class Home():
    """."""

    @home_blueprint.route("/api", methods=["GET", "POST"])
    def home():
        """."""
        return {"hello": "please authenticate :)"}

    @home_blueprint.route("/api/auth", methods=["POST"])
    def auth():
        """."""
        client_id = request.form.get("client_id")
        client_secret = request.form.get("client_secret")

        access_token = auth.request_access_token(
            client_id=client_id,
            client_secret=client_secret)

        if access_token:

            return {
                "access_token": access_token,
                "token_type": "JWT",
                "expires_in": auth.lifetime
            }

        return {"i'm": "sorry"}
