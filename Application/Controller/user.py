"""."""
from flask import render_template, session
from Model.user import Users
from flask import Blueprint

user_blueprint = Blueprint("user_blueprint", __name__)


class User():
    """."""

    def __init__(self):
        """."""

    @user_blueprint.before_request
    def before_request():
        """."""
        return "nope"
        if session.get("id"):
            pass
        else:
            return "nope"

    @user_blueprint.route("/user")
    def user():
        """."""
        _users = Users.query.all()

        r = [
            {"name": i.name, "email": i.email} for i in _users]

        if r:
            r = r[0]

        return render_template("user.html", name=r["name"], email=r["email"])
