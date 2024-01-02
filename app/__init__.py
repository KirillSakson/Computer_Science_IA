from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "login"


from app.controllers.home_controller import *
from app.controllers import auth_controller, boardgame_controller
from app.models.boardgame import *
from app.models.ranking import Ranking


if __name__ == "__main__":
    app.run(debug=True)
