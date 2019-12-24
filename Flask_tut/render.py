from flask import *
app=Flask(__name__)
@app.route('/<int:name>')
def home(name):
    return render_template('trysome.html',cname=name)
if __name__ == '__main__':
    app.run(debug=True)