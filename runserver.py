from flask import request,render_template,flash,abort,url_for,redirect,session,Flask
from app import app

from app.api.controller import api_email_sync
from app.email.controller import email_web


@app.route('/')
def hello_world():
    return redirect(url_for("redirect_from_api"))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)