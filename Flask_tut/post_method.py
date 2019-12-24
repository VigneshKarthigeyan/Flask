from flask import *
app=Flask(__name__)
@app.route('/login',methods=['GET'])
def login():
    un=request.form['un']
    pss=request.args.get('pss')
    if(un=='Vignesh' and pss=='Venkatesh'):
        return 'Successfully logged in';
    else:
        return 'wrong user name or password';
if __name__ == '__main__':
    app.run(debug=True)