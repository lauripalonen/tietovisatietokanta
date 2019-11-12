from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

errMsgQ = "Question field must be atleast 2 characters long"
errMsgA = "Answer field cannot be empty"

class QuestionForm(FlaskForm):
    question = StringField("Question", [validators.Length(min=2, message=errMsgQ)])
    answer = StringField("Answer", [validators.Length(min=1, message=errMsgA)])
    correct = BooleanField("Answered correctly")
     
    class Meta:
        csrf = False

class EditForm(FlaskForm):
    question = StringField("Question", [validators.Length(min=2, message=errMsgQ)])
    answer = StringField("Answer", [validators.Length(min=1, message=errMsgA)])
    correct = BooleanField("Answered correctly")

    class Meta:
        csrf = False
