from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, bcrypt, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm
from application.teams.models import Team

import os


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    if os.environ.get("HEROKU"):

        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

        if not user:
            return render_template("auth/loginform.html", form=form,
                                   error="No such username")
    else:

        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            return render_template("auth/loginform.html", form=form,
                                   error="No such username")

        if not bcrypt.check_password_hash(user.password, form.password.data):
           return render_template("auth/loginform.html", form=form,
                                   error="Incorrect password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/signup", methods=["GET", "POST"])
def auth_signup():
    if request.method == "GET":
        return render_template("auth/signupform.html", form=SignupForm())

    form = SignupForm(request.form)
    if not form.validate():
        return render_template("auth/signupform.html", form=form, error="Username or password too short")


    username = form.username.data
    team_name = form.team.data
    role_id = 2

    if os.environ.get("HEROKU"):
        password = form.password.data

    else:
        password = bcrypt.generate_password_hash(form.password.data)

    user = User.query.filter_by(username=username).first()

    if user:
        return render_template("auth/signupform.html", form=form, error="Username already exists")

    new_user = User(username=username, password=password, role_id=role_id)
    db.session().add(new_user)

    team = Team.query.filter_by(name=team_name).first()

    if not team:
        team = Team(team_name)
        db.session().add(team)

    db.session().commit()

    created_user = User.query.filter_by(username=username).first()

    new_user.team_id = team.id
    team.members.append(created_user)

    db.session().commit()

    login_user(new_user)
    return redirect(url_for("index"))