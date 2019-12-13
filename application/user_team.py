from application import db
from sqlalchemy.sql import text


user_team = db.Table('user_team', 
    db.Column('user_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')))

def clear_table():
        stmt = text("DELETE FROM user_team WHERE user_team.user_id !="
                   " (SELECT id FROM account WHERE username = 'ADMIN')")

        db.engine.execute(stmt)

        return print("user_team table cleared")