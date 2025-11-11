from flask import Flask


app = Flask(__name__)


@app.route("/")
def main():
    return "test"


app.run(host="0.0.0.0", port=5004)

