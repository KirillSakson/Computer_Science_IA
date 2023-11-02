from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, current_user, logout_user
from app.models.user import User
from app.forms.login_form import LoginForm
from app.forms.registration_form import RegistrationForm
from app.forms.user_edit_form import EditForm


@app.route("/registration/", methods=["post", "get"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you've just registered successfully!", "success")
        return redirect(url_for("login"))
    return render_template("auth/registration.html", title="Registration", form=form)


@app.route("/login/", methods=["get", "post"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("home")
            return redirect(next_page)
        flash("Incorrect username/password", "danger")
        return redirect(url_for("login"))
    return render_template("auth/login.html", form=form)


@app.route("/logout/", methods=["get", "post"])
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out!", "success")
    return redirect(url_for("login"))


@app.route("/account/")
@login_required
def account():
    return render_template("home/account.html")


@app.route("/edit_profile/", methods=["get", "post"])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.set_password(form.password.data)
        db.session.commit()
        flash("Congratulations, you've just edited your account data successfully!", "success")
        logout_user()
        return redirect(url_for("login"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template("auth/edit.html", title="Editing account data", form=form)
