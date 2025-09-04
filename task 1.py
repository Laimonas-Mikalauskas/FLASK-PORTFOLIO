from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///projects.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

__import__("style.css")
