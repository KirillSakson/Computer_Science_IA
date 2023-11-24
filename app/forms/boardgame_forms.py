from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class AddBoardgameForm(FlaskForm):
    name = StringField("Game's name", validators=[DataRequired()])
    min_players = IntegerField("Minimum possible players", validators=[DataRequired()])
    max_players = IntegerField("Maximum possible players", validators=[DataRequired()])
    description = StringField("Game's description", validators=[DataRequired()])
    ranking = IntegerField("Rate the game (1-5)", validators=[DataRequired()])
    submit = SubmitField("Done!")

    def get_min_players(self):
        return self.min_players.data

    def validate_ranking(self, ranking):
        if not 1 <= ranking.data <= 5:
            raise ValidationError("Rate the game in range between 1 and 5")

    def validate_min_players(self, min_players):
        if min_players.data < 1:
            raise ValidationError("Minimum amount of players is 1")

    def validate_max_players(self, max_players):
        if max_players.data < self.get_min_players():
            raise ValidationError("Maximum amount of players cannot be less than the minimum amount of them")


class EditBoardgameForm(FlaskForm):
    name = StringField("Game's name", validators=[DataRequired()])
    min_players = IntegerField("Minimum possible players", validators=[DataRequired()])
    max_players = IntegerField("Maximum possible players", validators=[DataRequired()])
    description = StringField("Game's description", validators=[DataRequired()])
    submit = SubmitField("Done!")
