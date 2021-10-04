from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f"{username}'s profile"


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('index', next='/'))
#     print(url_for('profile', username='John Doe'))


with app.test_request_context():
    static_url = url_for('static', filename='style.css')
    print(static_url)
