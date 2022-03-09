from app import app
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask
import requests

@app.route("/email_service")
def email_service():
    a = requests.get("http://localhost:8888/api_email_sync/test1")
    print(a)
    print(a.text)
    return "Inside of email_service"

@app.route("/email_service/redirect_from_api")
def redirect_from_api():
    return "From api"

@app.route("/email_service/first_page")
def first_page():
    return render_template("email/templates/index.html")