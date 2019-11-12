from application import app, db
from flask import redirect, render_template, request, url_for
from application.questions.models import Question

@app.route("/questions/", methods=["GET"])
def questions_index():
  return render_template("questions/list.html", questions = Question.query.all())

@app.route("/questions/new/")
def questions_form():
  return render_template("questions/new.html")

@app.route("/questions/<question_id>", methods=["GET"])
def edit_form(question_id):
  q = Question.query.get(question_id)
  c = "checked" if q.answeredCorrectly == True else ""
  return render_template("questions/edit.html", question=q, checked=c)

@app.route("/questions/<question_id>", methods=["POST"])
def questions_update(question_id):
  q = Question.query.get(question_id)
  q.question = request.form.get("question")
  q.answer = request.form.get("answer")
  c = (request.form.get("answeredCorrectly") != None)
  q.answeredCorrectly = c
  db.session().commit()

  return redirect(url_for("questions_index"))

@app.route("/questions/", methods=["POST"])
def questions_create():
  q = request.form.get("question")
  a = request.form.get("answer")
  c = (request.form.get("answeredCorrectly") != None)
  qObject = Question(question=q, answer=a, answeredCorrectly = c)

  db.session().add(qObject)
  db.session().commit()

  return redirect(url_for("questions_index"))

