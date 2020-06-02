"""."""
from flask import render_template, request, session
from Model.user import Users
import bcrypt


class Home():
    """."""

    def __init__(self):
        """."""

    def index(self):
        """."""
        return render_template("index.html")

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
