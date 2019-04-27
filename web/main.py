import flask
app=flask.Flask("MyPage")

@app.route("/")
def hello():
    return """"
    <h1>helloworle</h1>
    <input />
    """