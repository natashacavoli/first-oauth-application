"""."""
from flask import request, Blueprint
from Auth.auth import Auth
from Model.user import User as UserModel
from Model.client import Client
from Model.db import db


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

        if not auth.validate_access_token(access_token):

            return _error, 400

        pass

    @user_blueprint.route("/api/me", methods=["POST"])
    def user():
        """."""
        _auth_header = request.headers.get("Authorization")

        access_token = _auth_header.split()[1]

        data = auth.decode_access_token(access_token)

        client_id = data.get("client_id")

        me = db.session.query(UserModel).join(
            Client, UserModel.id == Client.id).filter_by(
            client_id=client_id).first()

        if me:
            return {"name": me.name, "email": me.email}

        return {"not", "found"}
