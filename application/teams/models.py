from application import db
from application import user_team
from application.auth.models import User

class Team(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    questions = db.relationship("Question", backref="team", lazy=True)
    users = db.relationship("User", secondary="user_team", backref=db.backref('teamos', lazy=True))

    def __init__(self, name):
        self.name = name
