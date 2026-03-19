from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<h1>this is a header</h1>"


if __name__ == "__main__":
    app.run(debug=True)