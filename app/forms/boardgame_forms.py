from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, ValidationError


class AddBoardgameForm(FlaskForm):
    name = StringField("Board game's name", validators=[DataRequired()])
    min_players = IntegerField("Minimum possible players", validators=[DataRequired()])
    max_players = IntegerField("Maximum possible players", validators=[DataRequired()])
    description = StringField("Short board game's description", validators=[DataRequired()])
    full_description = TextAreaField("Full board game's description and its rules", validators=[DataRequired()])
    ranking = IntegerField("Rate the board game (1-5)", validators=[DataRequired()])
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

    def validate_description(self, description):
        if len(description.data) > 200:
            raise ValidationError("Short description should have less than 200 symbols")

    def validate_full_description(self, full_description):
        if len(full_description.data) == 0:
            raise ValidationError("You should add some rules and a basic description at least")


class EditBoardgameForm(FlaskForm):
    name = StringField("Board game's name", validators=[DataRequired()])
    min_players = IntegerField("Minimum possible players", validators=[DataRequired()])
    max_players = IntegerField("Maximum possible players", validators=[DataRequired()])
    description = StringField("Short board game's description", validators=[DataRequired()])
    full_description = TextAreaField("Full board game's description and its rules", validators=[DataRequired()])
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

    def validate_description(self, description):
        if len(description.data) > 200:
            raise ValidationError("Short description should have less than 200 symbols")

    def validate_full_description(self, full_description):
        if len(full_description.data) == 0:
            raise ValidationError("You should add some rules and a basic description at least")
