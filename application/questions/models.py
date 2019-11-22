from application import db
import os

from sqlalchemy.sql import text

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    question = db.Column(db.String(144), nullable=False)
    answer = db.Column(db.String(144), nullable=False)
    category = db.Column(db.String(144))
    answered_correctly = db.Column(db.Boolean)
    quiz_date = db.Column(db.DateTime)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __init__(self, question, answer, category, answered_correctly, team_id):
        self.question = question
        self.answer = answer
        self.category = category
        self.answered_correctly = answered_correctly
        self.team_id  = team_id

    @staticmethod
    def find_correct_answers_by_category(category):
        stmt = text("SELECT COUNT(Question.id) AS count FROM Question"
                    " WHERE answered_correctly = 1"
                    " AND category ='\:category'").params(category=category)

        res = db.engine.execute(stmt)

        print("RESPONSE FOR QUERY: " + res)

        response = []
        for row in res:
            response.append({"count: ":row[0]})
        
        return response
    
    @staticmethod
    def find_hardest_category(team_id):
        if os.environ.get("HEROKU"):
            stmt = text("SELECT MIN(avg_answered_correctly), category FROM (SELECT AVG(answered_correctly::int::float4)"
                        " AS avg_answered_correctly, category FROM Question WHERE team_id=:team_id GROUP BY category)"
                        " AS avg_answers GROUP BY category").params(team_id=team_id)

        else: 
            stmt = text("SELECT MIN(avg_answered_correctly) AS average, category"
                        " FROM (SELECT AVG(question.answered_correctly) AS avg_answered_correctly,"
                        " category FROM Question WHERE team_id=:team_id"
                        " GROUP BY category) AS avg_answers").params(team_id=team_id)

        ResultProxy = db.engine.execute(stmt)

        ResultSet = ResultProxy.fetchone()
        avg = ResultSet[0]*100
        cat = ResultSet[1]
        
        return "{} ({} {} correct answers).".format(cat, avg, "%")