from flask import *
app=Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return 'Hi this is the home page'

@app.route('/student')
def student():
    return 'Hi this is the student page'
@app.route('/admin')
def admin():
    return 'Hi this is the admin page'
@app.route('/login/<asd>')
def login(asd):
    if (asd=='student'):
        return redirect(url_for('student'))
    elif (asd=='admin'):
        return redirect(url_for('admin'))
    else:
        return 'Invalid'
if __name__ == '__main__':
    app.run(debug=True)
