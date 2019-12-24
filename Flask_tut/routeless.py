from flask import Flask

app = Flask(__name__)
def vicky():
    return "hello, this is our first flask website";
def venky():
    return "hello, this is our second flask website";
app.add_url_rule('/','vicky',vicky)
if __name__ == '__main__':
    app.run(debug=True)