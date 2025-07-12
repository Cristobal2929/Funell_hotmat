from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

def send_email(receiver_email):
    sender_email = os.getenv('SENDER_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    subject = "Tu ebook gratuito está aquí"
    body = f"Gracias por registrarte! Descarga tu ebook aquí: [ENLACE_DE_EBOOK]\n\nAdemás, revisa esta oferta especial: [TU_LINK_DE_HOTMART]"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(f"Error enviando email: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        email = request.form.get('email')
        if Lead.query.filter_by(email=email).first():
            message = 'Este email ya está registrado.'
        else:
            new_lead = Lead(email=email)
            db.session.add(new_lead)
            db.session.commit()
            send_email(email)
            message = '¡Gracias! Revisa tu email para descargar el ebook.'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
