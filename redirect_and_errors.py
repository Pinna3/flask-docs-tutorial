from flask import render_template
from flask import Flask, abort, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)
    # This is never executed


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
