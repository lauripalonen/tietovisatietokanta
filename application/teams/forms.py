from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TeamForm(FlaskForm):
    team_name = StringField("Team", [validators.Length(min=1, message="Team name must be atleast 1 character long")])

    class Meta:
        csrf = False
