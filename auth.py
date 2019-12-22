from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def homepage():
    return render_template("homepage.html")

@main.route("/profile")
def profile():
    return "Welcome to your profile"