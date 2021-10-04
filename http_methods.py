from flask import Flask, request

app = Flask(__name__)


def do_the_login():
    """Login function"""
    pass


def show_login_form():
    """Login input form"""
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_login_form()
