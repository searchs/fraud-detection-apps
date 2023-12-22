from flask import Flask, jsonify, request
from http import HTTPStatus

"""Simple API in Flask to retrieve users with profession"""

app = Flask(__name__)


def get_users():
    usersdb = [
        {"id": 1, "name": "Charles", "role": "Software Engineer"},
        {"id": 2, "name": "Elena", "role": "Saberedowo Tailor"},
        {"id": 3, "name": "Deniyi", "role": "Oniroyin"},
        {"id": 4, "name": "Brown", "role": "Dokita"},
        {"id": 5, "name": "Debbie", "role": "Agbejoro"},
    ]
    return usersdb


@app.route("/")
def index():
    return jsonify([]), HTTPStatus.OK


@app.route("/users/")
def get_users_list():
    """Get all users if no name is specified and
    specified user is name is provided"""
    users_list = get_users()
    name = request.args.get("name")
    if not name:
        return jsonify(users_list), HTTPStatus.OK

    if name:
        users = next(
            (
                user
                for user in users_list
                if str(user["name"]).lower() == name.lower()
            ),
            None,
        )

        if not users:
            return jsonify([]), HTTPStatus.OK
        return jsonify(users), HTTPStatus.OK


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
