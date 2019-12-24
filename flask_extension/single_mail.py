from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vigneshkarthigeyan123@gmail.com'
app.config['MAIL_PASSWORD'] = '8220191439'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('12-2-19', sender = 'vigneshkarthigeyan123@gmail.com', recipients = ['vigneshkarthigeyan123@yahoo.com'])
   msg.body = "present flask message"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)