from flask import *
from flask_mail import Mail, Message
from random import *

app =Flask(__name__)
rand=randint(111111,999999)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vigneshkarthigeyan123@gmail.com'
app.config['MAIL_PASSWORD'] = '8220191439'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('OTP', sender = 'vigneshkarthigeyan123@gmail.com', recipients = ['vickykarthy123@gmail.com',])
   msg.body = str(rand)
   mail.send(msg)
   return render_template('verify.html')
@app.route("/Check",methods=['POST'])
def Check():
    eotp=request.form['otp']
    if rand == int(eotp):
        return 'otp is correct'
    else:
        return 'otp is incorrect'

if __name__ == '__main__':
   app.run(debug = True)