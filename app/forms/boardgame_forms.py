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

    def validate_ranking(self, ranking):
        if not 1 <= ranking.data <= 5:
            raise ValidationError("Rate the game in range between 1 and 5")


class EditBoardgameForm(FlaskForm):
    name = StringField("Game's name", validators=[DataRequired()])
    min_players = IntegerField("Minimum possible players", validators=[DataRequired()])
    max_players = IntegerField("Maximum possible players", validators=[DataRequired()])
    description = StringField("Game's description", validators=[DataRequired()])
    submit = SubmitField("Done!")
