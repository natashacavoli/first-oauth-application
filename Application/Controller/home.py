"""."""
from flask import render_template, request, redirect, session, Blueprint
from Model.user import User
from Model.db import db
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

        _user = User.query.filter(User.username == username).first()

        if _user:

            _hashed = bcrypt.hashpw(password, _user.password.encode("utf-8"))

            if _hashed.decode("utf-8") == _user.password:

                if _user.id not in session:

                    session["id"] = _user.id

                    return redirect("/me")

            return redirect("/error")

        return redirect("/error")

    @home_blueprint.route("/error")
    def error():
        """."""
        return render_template("error.html")

    @home_blueprint.route("/signup")
    def signup():
        """."""
        return render_template("signup.html")

    @home_blueprint.route("/register", methods=["POST"])
    def register():
        """."""
        name = request.form.get("name")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password").encode("utf-8")

        salt = bcrypt.gensalt()

        password = bcrypt.hashpw(password, salt).decode("utf-8")

        me = User(
            name=name,
            email=email,
            username=username,
            password=password)

        db.session.add(me)
        db.session.commit()

        return redirect("/")
