from flask import *
app=Flask(__name__)
@app.route('/')
def starting():
    return render_template('h_cookie.html')
@app.route('/home',methods=['POST'])
def home():
    user1=request.form['user']
    res=make_response(render_template('prt.html'))
    res.set_cookie('User Id',user1)
    return res;
if __name__ == '__main__':
    app.run(debug=True)