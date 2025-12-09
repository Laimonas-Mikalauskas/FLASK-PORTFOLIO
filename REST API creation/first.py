from flask import Flask, jsonify, request
from calendar import isleap

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        some_json = request.get_json()
        return jsonify({"you sent": some_json})

    if request.method == "GET":
        return jsonify({"about": "Hello world"})


@app.route("/keliamieji/<int:metai>")
def keliamieji(metai):
    if isleap(metai):
        return jsonify({"result": "Keliamieji"})
    else:
        return jsonify({"result": "NEkeliamieji"})

if __name__ == '__main__':
    app.run(debug=True)