from application import db

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

  def __init__(self, question, answer, answeredCorrectly):
      self.question = question
      self.answer = answer
      self.answeredCorrectly = answeredCorrectly


  
