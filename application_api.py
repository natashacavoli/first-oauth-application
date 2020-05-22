"""."""
from flask import Flask
from Application.application import User


app = Flask(__name__)

u = User()


@app.before_request
def before_request():
    """."""
    pass


@app.route("/user")
def user():
    """."""
    return u.get_user()


if __name__ == "__main__":
    app.run(debug=True)
