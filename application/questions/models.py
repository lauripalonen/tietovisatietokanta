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
    quiz_date = db.Column(db.Date)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __init__(self, question, answer, category, answered_correctly, date, team_id):
        self.question = question
        self.answer = answer
        self.category = category
        self.answered_correctly = answered_correctly
        self.quiz_date = date
        self.team_id  = team_id

    @staticmethod
    def find_correct_answers_by_category(category):
        stmt = text("SELECT COUNT(Question.id) AS count FROM Question"
                    " WHERE answered_correctly = 1"
                    " AND category ='\:category'").params(category=category)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"count: ":row[0]})
        
        return response
    
    @staticmethod
    def find_hardest_category(team_id):
        if os.environ.get("HEROKU"):
            stmt = text("SELECT avg, category"
                        " FROM (SELECT AVG(answered_correctly::int::float4), category"
                        " FROM Question WHERE team_id=:team_id GROUP BY category) AS avg_correct"
                        " WHERE avg = (SELECT MIN(avg_correct.avg)"
                        " FROM (SELECT AVG(answered_correctly::int::float4)"
                        " FROM Question WHERE team_id=:team_id GROUP BY category) as avg_correct)").params(team_id=team_id)

        else: 
            stmt = text("SELECT MIN(avg_answered_correctly) AS average, category"
                        " FROM (SELECT AVG(question.answered_correctly) AS avg_answered_correctly,"
                        " category FROM Question WHERE team_id=:team_id"
                        " GROUP BY category) AS avg_answers").params(team_id=team_id)

        ResultProxy = db.engine.execute(stmt)

        ResultSet = ResultProxy.fetchone()
        avg = ResultSet[0]*100
        cat = ResultSet[1]

        if avg == 100:
            return "Your team has answered correctly to every question so far. Well done!"

        else: 
            return "Most difficult category: {} ({} {} correct answers).".format(cat, avg, "%")