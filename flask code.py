from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from my first Flask webApp!!!\nHOMEPAGE"

@app.route("/news")
def news():
    return "This is a main news page"

@app.route("/news/<int:item>")
def news_item(item):
    return f"This is new NR {item}"

@app.route("/<text>")
def any_route(text):
    return f"You entered the route {text}  There in no any resources"

if __name__ == "__main__":
    app.run()