from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    username = request.cookies.get('username')  # noqa:F841
    # use cookies.get(key) instead of cookies[key] to not get a KeyError is
    # the cookie is missing


@app.route('/')
def index():  # noqa:F811
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the_username')
    return resp
