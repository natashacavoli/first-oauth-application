"""."""
from flask import render_template, session, redirect, Blueprint
from Model.user import User as ModelUser
from Model.client import Client
from Model.db import db
import uuid
import secrets
import datetime


user_blueprint = Blueprint("user_blueprint", __name__)


class User():
    """."""

    def __init__(self):
        """."""

    @user_blueprint.before_request
    def before_request():
        """."""
        if session.get("id") and session.get("logged"):
            pass
        else:
            return redirect("/login")

    @user_blueprint.route("/me")
    def user():
        """."""
        user = ModelUser.query.filter(ModelUser.id == session.get("id")).\
            first()

        data = {"name": user.name, "email": user.email}

        return render_template("user.html", data=data)

    @user_blueprint.route("/me/api")
    def api():
        """."""
        result = Client.query.filter(Client.id == session.get("id")).\
            first()

        has_access = None

        data = {}

        if result:

            has_access = True

            data = {
                "client_id": result.client_id,
                "client_secret": result.client_secret
            }

        return render_template(
            "api.html",
            has_access=has_access,
            data=data)

    @user_blueprint.route("/me/api/get")
    def get_api():
        """."""
        result = Client.query.filter(Client.id == session.get("id")).\
            first()

        if result:

            return redirect("/me/api")

        client_id = uuid.uuid4()

        client_secret = secrets.token_hex(32)

        expires = datetime.datetime.now() + datetime.timedelta(days=365)

        client = Client(
            id=session.get("id"),
            client_id=client_id,
            client_secret=client_secret,
            expires=expires)

        db.session.add(client)
        db.session.commit()

        return redirect("/me/api")

    @user_blueprint.route("/me/api/revoke")
    def revoke_api():
        """."""
        Client.query.filter(Client.id == session.get("id")).\
            delete()

        db.session.commit()

        return redirect("/me/api")
