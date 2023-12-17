from app import db
from datetime import datetime


# table for favourite boardgames
user_boardgames = db.Table("user_boardgames",
                           db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
                           db.Column("boardgame_id", db.Integer(), db.ForeignKey("boardgames.id")))


class BoardGame(db.Model):
    __tablename__ = "boardgames"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))  # for author
    min_players = db.Column(db.Integer)
    max_players = db.Column(db.Integer)
    description = db.Column(db.String(100), nullable=False)
    full_description = db.Column(db.Text, nullable=False)
    rank = db.Column(db.Integer, default=0)
    votes = db.Column(db.Integer, default=0)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    users = db.relationship("User", secondary=user_boardgames, backref="favourite_boardgames")  # for favourite boardgames

    def get_rank(self):
        return round(self.rank/self.votes, 1) if self.votes != 0 else 0
