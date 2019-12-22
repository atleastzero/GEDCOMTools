from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return "This will be a login page."

@auth.route("/signup")
def signup():
    return "This will be a signup page."