from flask import redirect, render_template, request, url_for

from application import app, db
from application.questions.models import Question
from application.questions.forms import QuestionForm, EditForm

@app.route("/questions/", methods=["GET"])
def questions_index():
  return render_template("questions/list.html", questions = Question.query.all())

@app.route("/questions/new/")
def questions_form():
  return render_template("questions/new.html", form = QuestionForm())

@app.route("/questions/<question_id>", methods=["GET"])
def edit_form(question_id):
  q = Question.query.get(question_id)
  c = "checked" if q.answeredCorrectly == True else ""
  return render_template("questions/edit.html", question=q, checked=c, form = EditForm())

@app.route("/questions/<question_id>", methods=["POST"])
def questions_update(question_id):
  q = Question.query.get(question_id)
  form = EditForm(request.form)
  
  q.question = form.question.data
  q.answer = form.answer.data
  q.answeredCorrectly = form.correct.data
  db.session().commit()

  return redirect(url_for("questions_index"))

@app.route("/questions/", methods=["POST"])
def questions_create():
  form = QuestionForm(request.form)

  if not form.validate():
    return render_template("questions/new.html", form = form)

  q = Question(form.question.data, form.answer.data, form.correct.data)

  db.session().add(q)
  db.session().commit()

  return redirect(url_for("questions_index"))

