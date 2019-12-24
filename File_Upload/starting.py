from flask import *
app=Flask(__name__)
app.secret_key='vicky'
@app.route('/')
def home():
    return render_template('upfile.html')
@app.route('/upload',methods=['post'])
def upload():
    f=request.files['insert_file']
    f.save(f.filename)
    flash('file successfully uploaded')

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)