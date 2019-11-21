from application import db

from sqlalchemy.sql import text

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    question = db.Column(db.String(144), nullable=False)
    answer = db.Column(db.String(144), nullable=False)
    category = db.Column(db.String(144))
    answeredCorrectly = db.Column(db.Boolean)
    quizDate = db.Column(db.DateTime)

    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def __init__(self, question, answer, category, answeredCorrectly, team_id):
        self.question = question
        self.answer = answer
        self.category = category
        self.answeredCorrectly = answeredCorrectly
        self.team_id  = team_id

    @staticmethod
    def find_correct_answers_by_category(category):
        stmt = text("SELECT COUNT(Question.id) AS count FROM Question"
                    " WHERE answeredCorrectly = 1"
                    " AND category ='\:category'").params(category=category)

        res = db.engine.execute(stmt)

        print("RESPONSE FOR QUERY: " + res)

        response = []
        for row in res:
            response.append({"count: ":row[0]})
        
        return response
    
    @staticmethod
    def find_hardest_category(team_id):
        stmt = text("SELECT MIN(avg_answeredCorrectly) AS average, category"
                    " FROM (SELECT AVG(answeredCorrectly) AS avg_answeredCorrectly,"
                    " category FROM Question WHERE team_id=:team_id"
                    " GROUP BY category) AS avg_answers").params(team_id=team_id)

        ResultProxy = db.engine.execute(stmt)

        ResultSet = ResultProxy.fetchone()
        avg = ResultSet[0]*100
        cat = ResultSet[1]
        
        return "{} ({} {} correct answers).".format(cat, avg, "%")