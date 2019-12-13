from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField

class TeamForm(FlaskForm):
    team_name = StringField("Create new team", [validators.Length(min=1, message="Team name must be atleast 1 character long")])
    team_list = SelectField("List of teams", coerce=int)

    class Meta:
        csrf = False