from app import app
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask

@app.route("/email_service")
def email_service():
    return "Inside of email_service"

@app.route("/email_service/redirect_from_api")
def redirect_from_api():
    return "From api"

@app.route("/email_service/first_page")
def first_page():
    return render_template("email/templates/index.html")