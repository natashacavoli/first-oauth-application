"""."""
from flask import render_template, session, request, redirect, Blueprint
from Model.user import User as ModelUser
from Model.client import Client
from Model.db import db
import uuid
import secrets
import datetime
import bcrypt


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
        user = ModelUser.query.get(session.get("id"))

        data = {
            "name": user.name,
            "email": user.email,
            "username": user.username,
            "bio": user.bio}

        return render_template("user.html", data=data)

    @user_blueprint.route("/me/api")
    def api():
        """."""
        result = Client.query.get(session.get("id"))

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
        result = Client.query.get(session.get("id"))

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
        client = Client.query.get(session.get("id"))

        db.session.delete(client)

        db.session.commit()

        return redirect("/me/api")

    @user_blueprint.route("/me/change")
    def change():
        """."""
        user = ModelUser.query.get(session.get("id"))

        data = {
            "name": user.name,
            "email": user.email,
            "username": user.username,
            "bio": user.bio}

        return render_template("change.html", data=data)

    @user_blueprint.route("/me/change/update", methods=["POST"])
    def update_change():
        """."""
        bio = request.form.get("bio")
        name = request.form.get("name")
        password = request.form.get("password").encode("utf-8")

        if password:

            salt = bcrypt.gensalt()

            password = bcrypt.hashpw(password, salt).decode("utf-8")

        me = ModelUser.query.get(session.get("id"))

        if bio:
            me.bio = bio

        if name:
            me.name = name

        if password:
            me.password = password

        db.session.commit()

        return redirect("/me/change")
