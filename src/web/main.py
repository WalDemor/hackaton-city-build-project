from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def start():
    return redirect(url_for('home'))

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/initiative", methods=['GET', 'POST'])
def initiative():
    return render_template("initiative.html")

@app.route("/projects", methods=['GET', 'POST'])
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")