"""."""
from flask import render_template, request, session
from Model.user import Users
import bcrypt


class User():
    """."""

    def __init__(self):
        """."""

    def index(self):
        """."""
        return "oi"

    def user(self):
        """."""
        _users = Users.query.all()

        r = [
            {"name": i.name, "email": i.email} for i in _users]

        if r:
            r = r[0]

        return render_template("user.html", name=r["name"], email=r["email"])

    def login(self):
        """."""
        return render_template("login.html")

    def auth_login(self):
        """."""
        username = request.form.get("username")
        password = request.form.get("password").encode("utf-8")

        _user = Users.query.filter(Users.username == username).first()

        if _user:

            _hashed = bcrypt.hashpw(password, _user.password.encode("utf-8"))

            if _hashed.decode("utf-8") == _user.password:

                if _user.id not in session:

                    # session["id"] = _user.id

                    return "Ok :)"

            return "nope"

        return "nope"
