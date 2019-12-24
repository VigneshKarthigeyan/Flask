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
users=[{'name':'vicky','email':'vickykarthy123@gmail.com'},{'name':'venky','email':'vigneshkarthigeyan123@yahoo.com'}]

@app.route("/")
def index():
   for i in users:
       msg = Message('Hello %s' %i['name'], sender = 'vigneshkarthigeyan123@gmail.com', recipients = [i['email']])
       msg.body = "new multiple flask message"
       mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)