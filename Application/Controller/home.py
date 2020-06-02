"""."""
from flask import render_template, request, session
from Model.user import Users
from flask import Blueprint
import bcrypt


home_blueprint = Blueprint("home_blueprint", __name__)


class Home():
    """."""

    def __init__(self):
        """."""

    @home_blueprint.route("/")
    def index():
        """."""
        return render_template("index.html")

    @home_blueprint.route("/login")
    def login():
        """."""
        return render_template("login.html")

    @home_blueprint.route("/auth_login", methods=["POST"])
    def auth_login():
        """."""
        username = request.form.get("username")
        password = request.form.get("password").encode("utf-8")

        _user = Users.query.filter(Users.username == username).first()

        if _user:

            _hashed = bcrypt.hashpw(password, _user.password.encode("utf-8"))

            if _hashed.decode("utf-8") == _user.password:

                if _user.id not in session:

                    session["id"] = _user.id

                    return "Ok :)"

            return "nope"

        return "nope"