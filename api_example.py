from flask import jsonify
from flask import Flask, url_for

app = Flask(__name__)


def get_current_user():
    pass


@app.route('/me')
def me_api():
    user = get_current_user()
    return {
        'username': user.username,
        'theme': user.theme,
        'image': url_for('user_image', filename=user.image),
    }


def get_all_users():
    pass


@app.route('/users')
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])
