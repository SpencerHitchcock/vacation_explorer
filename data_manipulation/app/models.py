from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), index=True)
    state = db.Column(db.String(120), index=True, unique=True)
    date = db.Column(db.String(120), index=True, unique=True)
    abr = db.Column(db.String(28), index=True, unique=True)

    def __repr__(self):
        return '<Title {}>'.format(self.title)    