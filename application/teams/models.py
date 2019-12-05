from application import db
from application import user_team
from application.auth.models import User
from sqlalchemy.sql import text

class Team(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    questions = db.relationship("Question", backref="team", lazy=True)
    users = db.relationship("User", secondary="user_team", backref=db.backref('user_teams', lazy=True))

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_teams_of_a_user(user_id):
        stmt = text("SELECT id, name FROM team JOIN user_team"
                    " ON user_team.team_id=team.id"
                    " WHERE user_team.user_id=:user_id").params(user_id=user_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append([row[0], row[1]])

        

        return response