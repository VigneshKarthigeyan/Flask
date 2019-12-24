from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "hello, welcome to home website";
@app.route('/new/<asd>')
def new(asd):
    return "hello, welcome to new website "+ asd;



if __name__ == "__main__":
    app.run(debug=True)