from application import db

user_team = db.Table('user_team', 
    db.Column('user_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')))