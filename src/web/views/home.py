from flask import Blueprint, render_template


home = Blueprint('auth', __name__)


@home.route("/home", methods=['GET', 'POST'])
def home_():
    return render_template("home.html")