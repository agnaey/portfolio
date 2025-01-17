from flask import Flask, render_template,request
from flask_mail import Mail, Message

app=Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'agnaeyviswanath1234@gmail.com'
app.config['MAIL_PASSWORD'] = 'iggx ufix rrlq ibqr'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_mail',methods=['POST'])
def send_message():
    name=request.form['name']
    email=request.form['email']
    message=request.form['message']
    msg = Message(subject='Hello', sender=email, recipients=['agnaeyviswanath1234@gmail.com'])
    msg.body = f"From: {name}\n {email}\n\nMessage:\n{message}"
    mail.send(msg)
    return render_template('index.html', success=True)




app.run()

