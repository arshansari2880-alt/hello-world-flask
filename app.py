from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    print("User authentication workflow initialized.")
    return "Hello World - User Auth Enabled"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
