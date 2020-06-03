"""."""
from flask import render_template, session, Blueprint
from Model.user import User as ModelUser

user_blueprint = Blueprint("user_blueprint", __name__)


class User():
    """."""

    def __init__(self):
        """."""

    @user_blueprint.before_request
    def before_request():
        """."""
        if session.get("id"):
            pass
        else:
            return "nope"

    @user_blueprint.route("/me")
    def user():
        """."""
        _user = ModelUser.query.filter(ModelUser.id == session.get("id")).\
            first()

        r = {"name": _user.name, "email": _user.email}

        return render_template("user.html", name=r["name"], email=r["email"])
