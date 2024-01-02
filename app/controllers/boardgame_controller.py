from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models.boardgame import BoardGame
from app.forms.boardgame_forms import AddBoardgameForm, EditBoardgameForm
from app.models.ranking import Ranking


@app.route("/add_boardgame/", methods=["post", "get"])
@login_required
def add_boardgame():
    form = AddBoardgameForm()
    if form.validate_on_submit():
        boardgame = BoardGame(name=form.name.data, user_id=current_user.id, min_players=form.min_players.data,
                              max_players=form.max_players.data, description=form.description.data,
                              full_description=form.full_description.data)
        db.session.add(boardgame)
        db.session.commit()
        ranking = Ranking(user_id=current_user.id, boardgame_id=boardgame.id, rank=form.ranking.data)
        db.session.add(ranking)
        db.session.commit()
        flash("Congratulations, you've just added a new boardgame successfully!", "success")
        return redirect(url_for("home"))
    return render_template("boardgames/addboardgame.html", title="Adding new boardgame", form=form)


@app.route("/edit_boardgame/<int:boardgame_id>/", methods=["get", "post"])
@login_required
def edit_boardgame(boardgame_id):
    boardgame = BoardGame.query.get(boardgame_id)
    if boardgame.author == current_user:
        form = EditBoardgameForm()
        if form.validate_on_submit():
            boardgame.name = form.name.data
            boardgame.min_players = form.min_players.data
            boardgame.max_players = form.max_players.data
            boardgame.description = form.description.data
            boardgame.full_description = form.full_description.data
            db.session.commit()
            flash("Congratulations, you've just edited boardgame information successfully!", "success")
            return redirect(url_for("boardgame_profile", boardgame_id=boardgame_id))
        elif request.method == "GET":
            form.name.data = boardgame.name
            form.min_players.data = boardgame.min_players
            form.max_players.data = boardgame.max_players
            form.description.data = boardgame.description
            form.full_description.data = boardgame.full_description
        return render_template("boardgames/editboardgame.html", title="Editing boardgame information", form=form)
    else:
        flash("You cannot edit this boardgame's information", "danger")
        return redirect(url_for("boardgame_profile", boardgame_id=boardgame_id))


@app.route("/boardgame_profile/<int:boardgame_id>/")
@login_required
def boardgame_profile(boardgame_id):
    boardgame = BoardGame.query.get(boardgame_id)
    if boardgame is None:
        flash("Boardgame not found", "danger")
        return redirect(url_for("home"))
    full_description = boardgame.full_description.split("\n")
    return render_template("boardgames/profile.html", bg=boardgame, fd=full_description)


@app.route("/add_to_favourite/<int:bg_id>/")
@login_required
def add_to_favourite(bg_id):
    bg = BoardGame.query.get(bg_id)
    if bg is None:
        flash("Boardgame not found", "danger")
        return redirect(url_for("boardgame_profile", boardgame_id=bg_id))
    current_user.favourite_boardgames.append(bg)
    db.session.commit()
    flash("Boardgame added to favourite successfully", "success")
    return redirect(url_for("boardgame_profile", boardgame_id=bg_id))


@app.route("/remove_from_favourite/<int:bg_id>/")
@login_required
def remove_from_favourite(bg_id):
    bg = BoardGame.query.get(bg_id)
    if bg is None:
        flash("Boardgame not found", "danger")
        return redirect(url_for("boardgame_profile", boardgame_id=bg_id))
    current_user.favourite_boardgames.remove(bg)
    db.session.commit()
    flash("Boardgame removed from favourite successfully", "success")
    return redirect(url_for("boardgame_profile", boardgame_id=bg_id))


@app.route("/rank_boardgame/", methods=["post"])
@login_required
def rank_boardgame():
    mark, bg_id = request.form.get("rank"), request.form.get("bg_id")
    bg = BoardGame.query.get(bg_id)
    for line in bg.ranking_users:
        if line.user_id == current_user.id:
            line.rank = mark
            db.session.commit()
            break
    else:
        ranking = Ranking(user_id=current_user.id, boardgame_id=bg_id, rank=mark)
        db.session.add(ranking)
        db.session.commit()
    return redirect(url_for("boardgame_profile", boardgame_id=bg_id))
