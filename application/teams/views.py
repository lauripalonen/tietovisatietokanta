from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db, user_team
from application.auth.models import User
from application.teams.models import Team
from application.teams.forms import TeamForm


@app.route("/teams", methods=["GET", "POST"])
@login_required
def teams_form():

  user = User.query.filter_by(id=current_user.id).first()
  teams = Team.find_teams_of_a_user(current_user.id)
  teams_list = [(team[0], team[1]) for team in teams]
  
  form = TeamForm()
  form.team_list.choices = teams_list

  if request.method == "GET":

    return render_template("/teams/teamform.html", form=form, teams=teams)

  if request.method == "POST":
    form = TeamForm(request.form)
    name = form.team_name.data

    team = Team.query.filter_by(name=name).first()

    if team:
      user.user_teams.append(team)
      db.session().commit()
      return render_template("teams/teamform.html", form=form, teams=teams)

    new_team = Team(name)
    db.session().add(new_team)

    new_team.members.append(user)

    db.session().commit()

    return redirect(url_for("index"))