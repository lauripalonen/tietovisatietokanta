from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class QuestionForm(FlaskForm):
    question = StringField("Question")
    answer = StringField("Answer")
    correct = BooleanField("Answered correctly")
     
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    question = StringField("Question")
    answer = StringField("Answer")
    correct = BooleanField("Answered correctly")

    class Meta:
        csrf = False
