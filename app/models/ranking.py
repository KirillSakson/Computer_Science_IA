from app import db


class Ranking(db.Model):
    __tablename__ = "ranking"
    user_id = db.Column(db.ForeignKey("users.id"), primary_key=True)
    boardgame_id = db.Column(db.ForeignKey("boardgames.id"), primary_key=True)
    rank = db.Column(db.Integer)
    user = db.relationship("User", backref="rankings")
    boardgame = db.relationship("BoardGame", backref="rankings")
