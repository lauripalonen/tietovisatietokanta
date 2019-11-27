from application import db
from application import user_team

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    teams = db.relationship('Team', secondary="user_team", backref=db.backref('members', lazy=True))

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if(self.role_id == 0):
            return ["ADMIN"]
        else:
            return ["ANY"]

class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    role = db.Column(db.String(8), nullable=False)

    def __init__(self, role):
        self.role = role

