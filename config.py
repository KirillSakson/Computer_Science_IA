import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "gggTYJHvjvjbnhbkhHNBhn6t237rbhngf67NG6384TFNYNG6nn79"
    APP_NAME = "Computer Science IA"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
