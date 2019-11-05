from application import app 
from flask import render_template, request

@app.route("/questions/new")
def tasks_form():
  return render_template("questions/new.html")

@app.route("/questions/", methods=["POST"])
def question_create():
  print(request.form.get("question"))

  return "hello world!"

