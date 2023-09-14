from app import app, db


@app.route("/")
@app.route("/home/")
@app.route("/index/")
def home():
    return "HI!"
