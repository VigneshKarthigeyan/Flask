from flask import *
from flask_wtf import *
from wtforms import *
from create_form import *

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    iobj=Createclass()
    return render_template('details.html',form=iobj)
@app.route('/success',methods=['POST'])
def success():
    return 'successful'
if __name__ == '__main__':
    app.run(debug=True)