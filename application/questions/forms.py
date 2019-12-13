from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators
from wtforms.fields.html5 import DateField
from datetime import date

errMsgQ = "Question must be between 2 to 144 characters long"
errMsgA = "Answer must be between 1 to 144 characters long"
errMsgC = "Category must between 3 to 50 characters long"
errMsgD = "Please enter the quiz date"

class QuestionForm(FlaskForm):
    question = StringField("Question", [validators.Length(min=2, max=144, message=errMsgQ)])
    answer = StringField("Answer", [validators.Length(min=1, max=144, message=errMsgA)])
    category = StringField("Category", [validators.Length(min=3, max=50, message=errMsgC)])
    correct = BooleanField("Answered correctly")
    date = DateField("Date", [validators.DataRequired(message=errMsgD)], default=date.today)

    class Meta:
        csrf = False

class EditForm(FlaskForm):
    question = StringField("Question", [validators.Length(min=2, message=errMsgQ)])
    answer = StringField("Answer", [validators.Length(min=1, message=errMsgA)])
    category = StringField("Category", [validators.Length(min=3, message=errMsgC)])
    correct = BooleanField("Answered correctly")
    date = DateField("Date", [validators.DataRequired(message=errMsgD)], default=date.today)

    class Meta:
        csrf = False
