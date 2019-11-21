from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db, user_team
from application.auth.models import User
from application.teams.models import Team
from application.teams.forms import TeamForm


@app.route("/teams", methods=["GET", "POST"])
@login_required
def teams_form():

  if request.method == "GET":

    return render_template("/teams/teamform.html", form=TeamForm())

  if request.method == "POST":
    form = TeamForm(request.form)
    name = form.team_name.data

    team = Team.query.filter_by(name=name).first()

    if team:
      return render_template("teams/teamform.html", form=form, error="Teams already exists")

    new_team = Team(name)
    db.session().add(new_team)

    user = User.query.filter_by(username=current_user.username).first()
    new_team.userinos.append(user)

    team_id = Team.query.filter_by(name=name).first().id
    current_user.team_id = team_id

    db.session().commit()

    return redirect(url_for("index"))