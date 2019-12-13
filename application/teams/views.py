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

    if request.form["btn"] == "Add team":
        if request.method == "POST":
            form = TeamForm(request.form)
            name = form.team_name.data

            team = Team.query.filter_by(name=name).first()

            if team:
                user.user_teams.append(team)
                db.session().commit()
                teams = Team.find_teams_of_a_user(current_user.id)
                form = TeamForm()

                return redirect(url_for("teams_form"))

            new_team = Team(name)
            db.session().add(new_team)

            new_team.members.append(user)

            db.session().commit()

            return redirect(url_for("teams_form"))

    if request.form["btn"] == "Modify team":
        if request.method == "POST":
            form = TeamForm(request.form)
            selected_id = form.team_list.data

            return redirect(url_for('teams_edit', team_id=selected_id))


@app.route("/editteam/<team_id>", methods=["GET", "POST", "PUT"])
@login_required
def teams_edit(team_id):
    teams = Team.find_teams_of_a_user(current_user.id)
    team_ids = [team[0] for team in teams]
    form = TeamForm()
    team = Team.query.filter_by(id=team_id).first()

    if request.method == "GET":
        if int(team_id) in team_ids:
            return render_template("/teams/editteam.html", team=team, form=form)
        else:
            print("Team is not a current user's team")
            return redirect(url_for("index"))

    if request.form["btn"] == "Set as representive":
        user = User.query.filter_by(id=current_user.id).first()
        user.team_id = team_id
        db.session().commit()
        return render_template("/teams/editteam.html", team=team, form=form)

    if request.form["btn"] == "Change name":
        if request.method == "POST":
            form = TeamForm(request.form)
            new_name = form.team_name.data
            team.name = new_name
            db.session().commit()
            return render_template("/teams/editteam.html", team=team, form=form)

    if request.form["btn"] == "Remove from my teams":
        if request.method == "POST":
            user = User.query.filter_by(id=current_user.id).first()

            if (user.team_id == int(team_id)):
                errorMsg = "Cannot remove representive team. Set another team as reprsentive team first."
                return render_template("/teams/editteam.html", team=team, form=form, error=errorMsg)

            else:
                user.remove_team(team_id)

                return redirect(url_for('teams_form'))
