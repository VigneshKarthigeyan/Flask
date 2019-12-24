from flask import *
from flask_mail import *
app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='vigneshkarthigeyan123@gmail.com'
app.config['MAIL_PASSWORD']='8220191439'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

@app.route('/')
def home():
    fi=app.open_resource('D:\desktop wallpapers\htiger.jpg')
    mes=Message('Subject mail',sender='vigneshkarthigeyan123@gmail.com',recipients=['vickykarthy123@gmail.com'])
    mes.body='This is the message sent via the flask framework'
    mes.attach('htiger.jpg','image/png',fi.read())
    mail.send(mes)
    return 'message sent'

if __name__ == '__main__':
    app.run(debug=True)