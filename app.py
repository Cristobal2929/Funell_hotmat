from flask import Flask, request, render_template
import serverless_wsgi
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

app = Flask(__name__)

EMAIL_ADDRESS = os.getenv('SENDER_EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

LINK_GUIA = 'https://drive.google.com/file/d/tu-guia.pdf'
LINK_VENTA = 'https://go.hotmart.com/tu-enlace-afiliado'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            # Enviar email
            try:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = email
                msg['Subject'] = 'Tu guía Mentalidad del Éxito'

                body = f"""
                Hola!

                Gracias por solicitar tu guía gratuita "Mentalidad del Éxito".

                ✅ DESCARGA tu guía aquí: {LINK_GUIA}

                🔥 Además, te recomiendo el ebook completo que ha ayudado a miles:

                👉 Consíguelo aquí: {LINK_VENTA}

                ¡Éxito en tu camino!
                """

                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
                server.quit()

                return render_template('index.html', success=True)
            except Exception as e:
                return render_template('index.html', error=str(e))
        else:
            return render_template('index.html', error="Por favor ingresa un email válido.")
    return render_template('index.html')

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
if __name__ == "__main__":
    app.run()
