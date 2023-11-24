from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.boardgame import BoardGame
from app.forms.boardgame_forms import AddBoardgameForm, EditBoardgameForm


@app.route("/add_boardgame/", methods=["post", "get"])
@login_required
def add_boardgame():
    form = AddBoardgameForm()
    if form.validate_on_submit():
        boardgame = BoardGame(name=form.name.data, user_id=current_user.id, min_players=form.min_players.data,
                              max_players=form.max_players.data, description=form.description.data,
                              rank=form.ranking.data, votes=1)
        db.session.add(boardgame)
        db.session.commit()
        flash("Congratulations, you've just added a new boardgame successfully!", "success")
        return redirect(url_for("home"))
    return render_template("boardgames/addboardgame.html", title="Adding new boardgame", form=form)


@app.route("/edit_boardgame/<int:boardgame_id>/", methods=["get", "post"])
@login_required
def edit_boardgame(boardgame_id):
    boardgame = BoardGame.query.get(boardgame_id)
    form = EditBoardgameForm()
    if form.validate_on_submit():
        boardgame.name = form.name.data
        boardgame.min_players = form.min_players.data
        boardgame.max_players = form.max_players.data
        boardgame.description = form.description.data
        db.session.commit()
        flash("Congratulations, you've just edited boardgame information successfully!", "success")
        return redirect(url_for("home"))
    elif request.method == "GET":
        form.name.data = boardgame.name
        form.min_players.data = boardgame.min_players
        form.max_players.data = boardgame.max_players
        form.description.data = boardgame.description
    return render_template("boardgames/editboardgame.html", title="Editing boardgame information", form=form)


@app.route("/boardgame_profile/<int:boardgame_id>/")
@login_required
def boardgame_profile(boardgame_id):
    boardgame = BoardGame.query.get(boardgame_id)
    if boardgame is None:
        flash("Boardgame not found", "danger")
        return redirect(url_for("home"))
    return render_template("boardgames/profile.html", bg=boardgame)
