from application import db
from application import user_team
from application.auth.models import User
from sqlalchemy.sql import text
import os

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

    @staticmethod
    def find_team_with_most_correct_answers():
        if os.environ.get("HEROKU"):
            stmt = text("SELECT name, AVG(answered_correctly::int::float4)"
                        " AS avg FROM Team JOIN Question ON question.team_id = team.id"
                        " GROUP BY name ORDER BY avg DESC limit 1")

        else: 
            stmt = text("SELECT name, AVG(answered_correctly) AS avg"
                        " FROM Team JOIN Question ON question.team_id = team.id"
                        " GROUP BY team.name ORDER BY avg DESC limit 1")

        ResultProxy = db.engine.execute(stmt)

        ResultSet = ResultProxy.fetchone()

        if ResultSet == None:
            return ""

        team = ResultSet[0]
        avg = ResultSet[1]*100
        
        return "Team with highest average of correct answers ({}{}): {}".format(avg, "%", team)
