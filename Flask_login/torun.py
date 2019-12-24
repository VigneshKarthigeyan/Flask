from flask import *
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('start.html')
@app.route('/check',methods=['POST'])
def check():
    user=request.form['un']
    pss=request.form['passw']
    if pss=='qwerty':
        resp=make_response(render_template('success.html'))
        resp.set_cookie('USER ID',user)
        return resp
    else:
        return redirect(url_for('failed'))
@app.route('/view')
def view():
    asd=request.cookies.get('USER ID')
    return 'Welcome '+ asd
@app.route('/failed')
def failed():
    return render_template('failure.html')
@app.route('/redo')
def redo():
    return render_template('start.html')
@app.route('/check1')
def check1():
    return 'checking the check'
if __name__ == '__main__':
    app.run(debug=True)