from app import db


# table for favourite boardgames
user_boardgames = db.Table("user_boardgames",
                           db.Column("user_id", db.Integer(), db.ForeignKey("users.id")),
                           db.Column("boardgame_id", db.Integer(), db.ForeignKey("boardgames.id")))


class BoardGame(db.Model):
    __tablename__ = "boardgames"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))  # for author
    min_players = db.Column(db.Integer())
    max_players = db.Column(db.Integer())
    description = db.Column(db.String(), nullable=False)
    rank = db.Column(db.Integer())
    votes = db.Column(db.Integer())
    users = db.relationship("User", secondary=user_boardgames, backref="boardgames")  # for favourite boardgames
