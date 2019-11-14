from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

errMsgU = "Username must be atleast 1 character long"
errMsgPw = "Password must be 5 characters long"

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class SignupForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=1, message=errMsgU)])
    password = PasswordField("Password", [validators.Length(min=5, message=errMsgPw)])

    class Meta:
        csrf = False
