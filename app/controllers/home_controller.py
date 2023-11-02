from app import app
from flask import render_template
from flask_login import login_required


@app.route("/")
def about():
    return render_template("about.html")


@app.route("/home")
@login_required
def home():
    return render_template("home/home.html")


@app.route("/favourite/")
@login_required
def favourite():
    return render_template("home/favourite.html")


@app.route("/bestranked/")
@login_required
def bestranked():
    return render_template("home/bestranked.html")
