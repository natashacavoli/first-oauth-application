"""."""
from flask import Flask
from Model.db import db
from Controller.home import home_blueprint
from Controller.user import user_blueprint


app = Flask(__name__)

_con = ""

app.config["SQLALCHEMY_DATABASE_URI"] = _con

app.secret_key = "secret_key"

app.config["SESSION_TYPE"] = "filesystem"

app.register_blueprint(user_blueprint)
app.register_blueprint(home_blueprint)

db.init_app(app)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
