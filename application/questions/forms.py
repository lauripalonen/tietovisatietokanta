from flask_wtf import FlaskForm
from wtforms import StringField

class QuestionForm(FlaskForm)
    question = StringField("Question")
     
    class Meta:
        csrf = False