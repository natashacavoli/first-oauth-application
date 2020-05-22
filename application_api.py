"""."""
from flask import Flask, request
from Auth.auth import Auth
from Application.application import User


app = Flask(__name__)

_user = User()
_auth = Auth()


@app.before_request
def before_request():
    """."""
    _auth_header = request.headers.get("Authorization")

    _error = {"i'm": "sorry"}

    if not _auth_header:

        return _error

    try:
        access_token = _auth_header.split()[1]
    except:
        access_token = None

    if not access_token:

        return _error

    if not _auth._verify_access_token(access_token):

        return _error

    pass


@app.route("/user")
def user():
    """."""
    return _user.get_user()


if __name__ == "__main__":
    app.run(debug=True)
