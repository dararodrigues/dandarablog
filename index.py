from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"



@app.route("/contatos")
def contacts():
    return"Diga o que voce quer"


if __name__ == '__main__':
    app.run(debug=True)
