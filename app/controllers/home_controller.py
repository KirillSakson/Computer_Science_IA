from math import ceil
from app import app, db
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models.boardgame import BoardGame
from random import shuffle
from sqlalchemy import func


def split_list(bgs):
    if len(bgs) == 0:
        return []
    n = ceil(len(bgs) / 4)
    boardgames = []
    for i in range(n):
        boardgames.append(bgs[4 * i:4 * i + 4])
    return boardgames

@app.route("/")
def about():
    return render_template("about.html")


@app.route("/home/")
@login_required
def home():
    bgs1 = BoardGame.query.all()
    bgs2 = current_user.favourite_boardgames
    bgs3 = current_user.boardgames_created
    shuffle(bgs1), shuffle(bgs2), shuffle(bgs3)
    return render_template("home/home.html", bgs1=bgs1[:3], bgs2=bgs2[:3], bgs3=bgs3[:3])


@app.route("/favourite/")
@login_required
def favourite():
    bgs = current_user.favourite_boardgames
    boardgames = split_list(bgs)
    if not boardgames:
        flash("There are no favourite boardgames yet", "warning")
        return redirect(url_for("home"))
    else:
        return render_template("home/favourite.html", boardgames=boardgames)


@app.route("/all_boardgames/")
@login_required
def all_boardgames():
    order_query = request.args.get("order", "")
    if order_query == "name":
        bgs = BoardGame.query.order_by(func.lower(BoardGame.name)).all()
    elif order_query == "date":
        bgs = BoardGame.query.order_by(BoardGame.updated_on).all()
    elif order_query == "rank":
        bgs = BoardGame.query.order_by(db.desc(BoardGame.rank / BoardGame.votes)).all()
    else:
        bgs = BoardGame.query.all()
    boardgames = split_list(bgs)
    if not boardgames:
        flash("There are no boardgames created yet", "warning")
        return redirect(url_for("add_boardgame"))
    else:
        return render_template("home/allboardgames.html", boardgames=boardgames)


@app.route("/my_boardgames/")
@login_required
def my_boardgames():
    bgs = current_user.boardgames_created
    boardgames = split_list(bgs)
    if not boardgames:
        flash("You still have not added any boardgame", "warning")
        return redirect(url_for("add_boardgame"))
    else:
        return render_template("home/myboardgames.html", boardgames=boardgames)


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
    boardgames = split_list(bgs)
    if not boardgames:
        flash("There are no boardgames that contain anything from the query", "danger")
        return redirect(url_for("home"))
    else:
        return render_template("home/search.html", boardgames=boardgames)
