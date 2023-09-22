from app import app, db
from flask import render_template


@app.route("/")
@app.route("/home/")
@app.route("/index/")
def home():
    return render_template("home/index.html")
