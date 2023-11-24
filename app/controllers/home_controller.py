import math

from app import app, db
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from app.models.boardgame import BoardGame
from random import shuffle


@app.route("/")
def about():
    return render_template("about.html")


@app.route("/home/")
@login_required
def home():
    bgs1 = BoardGame.query.all()
    shuffle(bgs1)
    if len(bgs1) > 3:
        bgs1 = bgs1[:3]
    return render_template("home/home.html", bgs1=bgs1)


@app.route("/favourite/")
@login_required
def favourite():
    return render_template("home/favourite.html")


@app.route("/bestranked/")
@login_required
def bestranked():
    return render_template("home/bestranked.html")


@app.route("/mygames/")
@login_required
def mygames():
    return render_template("home/mygames.html")


@app.route("/search/")
@login_required
def search():
    search_query = request.args.get("query", "")
    if search_query == "":
        flash("Query parameter not found", "danger")
        return redirect(url_for("home"))
    bgs = []
    for word in search_query.split():
        bgs_name = db.session.query(BoardGame).filter((BoardGame.name.contains(word)) | BoardGame.description.contains(word)).all()
        for bg in bgs_name:
            if bg not in bgs:
                bgs.append(bg)
    if len(bgs) == 0:
        flash("There are no boardgames that contain anything from the query", "danger")
        return redirect(url_for("home"))
    n = math.ceil(len(bgs) / 3)
    boardgames = []
    for i in range(n):
        boardgames.append(bgs[3*i:3*i+3])
    return render_template("home/search.html", boardgames=boardgames)

# {% if not loop.first %} offset-sm-1 {% endif %}