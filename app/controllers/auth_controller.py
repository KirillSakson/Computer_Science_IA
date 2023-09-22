from app import app, db


@app.route("/registration/", methods=["post", "get"])
def registration():
    pass


@app.route("/login/", methods=["get", "post"])
def login():
    pass


@app.route("/logout/", methods=["get", "post"])
def logout():
    pass
