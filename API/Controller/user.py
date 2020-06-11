"""."""
from flask import request, Blueprint
from Auth.auth import Auth


user_blueprint = Blueprint("user_blueprint", __name__)

auth = Auth()


class User():
    """."""

    @user_blueprint.before_request
    def before_request():
        """."""
        _auth_header = request.headers.get("Authorization")

        _error = {"i'm": "sorry"}

        if not _auth_header:

            return _error, 400

        try:
            access_token = _auth_header.split()[1]
        except:
            access_token = None

        if not access_token:

            return _error, 400

        if not auth.verify_access_token(access_token):

            return _error, 400

        pass

    @user_blueprint.route("/api/hi", methods=["POST"])
    def user():
        """."""
        return "oi"
