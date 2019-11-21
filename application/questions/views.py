from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.questions.models import Question
from application.questions.forms import QuestionForm, EditForm

from application.teams.models import Team


@app.route("/questions/", methods=["GET"])
@login_required
def questions_index():
    team = current_user.team_id
    questions = Question.query.filter_by(team_id=current_user.team_id)

    if (team and questions.first()):
        return render_template("questions/list.html",
                               questions=questions,
                               hardest_category=Question.find_hardest_category(team_id=team))

    return redirect(url_for("index"))


@app.route("/questions/new/")
@login_required
def questions_form():
    return render_template("questions/new.html", form=QuestionForm())


@app.route("/questions/<question_id>", methods=["GET"])
@login_required
def edit_form(question_id):
    q = Question.query.get(question_id)
    c = "checked" if q.answeredCorrectly == True else ""
    return render_template("questions/edit.html", question=q, checked=c, form=EditForm())


@app.route("/questions/<question_id>", methods=["POST"])
@login_required
def questions_update(question_id):
    q = Question.query.get(question_id)
    form = EditForm(request.form)

    q.question = form.question.data
    q.answer = form.answer.data
    q.category = form.category.data
    q.answeredCorrectly = form.correct.data
    db.session().commit()

    return redirect(url_for("questions_index"))


@app.route("/questions/", methods=["POST"])
@login_required
def questions_create():
    form = QuestionForm(request.form)

    if not form.validate():
        return render_template("questions/new.html", form=form)

    q = Question(
        form.question.data,
        form.answer.data,
        form.category.data,
        form.correct.data,
        current_user.team_id)

    db.session().add(q)
    db.session().commit()

    return redirect(url_for("questions_index"))


@app.route("/questions/<question_id>/delete", methods=["POST"])
@login_required
def questions_delete(question_id):
    q = Question.query.get(question_id)
    db.session().delete(q)
    db.session().commit()

    print("Question deleted!")

    return redirect(url_for("questions_index"))
