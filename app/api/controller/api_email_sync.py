from flask import request,render_template,flash,abort,url_for,redirect,session,Flask
from app import app
import json

@app.route("/api_email_sync/test1")
def test1():
    return json.dumps({"a":1})

@app.route("/api_email_sync/send_back")
def test2():
    return redirect(url_for("redirect_from_api"))
