"""."""
from flask import Flask
from Auth.auth import Auth

app = Flask(__name__)

_auth = Auth()


@app.route("/auth", methods=["POST"])
def auth():
    """."""
    access_token = _auth._generate_access_token()

    data = {
        "access_token": access_token,
        "token_type": "JWT",
        "expires_in": _auth.get_lifetime()
    }

    return data


if __name__ == "__main__":
    app.run(debug=True, port=5001)
