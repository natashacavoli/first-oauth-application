"""."""
from flask import Flask
from Model.db import db
from Controller import user, home


app = Flask(__name__)

_con = ""

app.config["SQLALCHEMY_DATABASE_URI"] = _con

app.secret_key = "secret_key"

app.config["SESSION_TYPE"] = "filesystem"

db.init_app(app)

user = user.User()
home = home.Home()

app.add_url_rule("/", view_func=home.index)
app.add_url_rule("/login", view_func=home.login)
app.add_url_rule("/auth_login", view_func=home.auth_login, methods=["POST"])
app.add_url_rule("/user", view_func=user.user)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
