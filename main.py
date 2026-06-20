import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openai
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuración de APIs
openai.api_key = os.environ.get("OPENAI_API_KEY")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_USER = "tu_correo@gmail.com" # Cambia esto por tu email real

# Conexión Sheets
creds_dict = json.loads(os.environ.get("GOOGLE_CREDENTIALS"))
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gc = gspread.authorize(creds)
worksheet = gc.open("bot-growth-flow-1").sheet1

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    try:
        cliente = request.form.get('cliente')
        producto = request.form.get('producto')
        monto = request.form.get('monto')
        
        worksheet.append_row([cliente, producto, monto])
        
        prompt = f"Escribe un guion de ventas persuasivo para vender {producto} a {cliente} por {monto}."
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        guion = response.choices[0].message.content
        
        msg = EmailMessage()
        msg.set_content(guion)
        msg['Subject'] = f'Nuevo Trato: {cliente}'
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_USER 

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        
        return f"<h1>Trato registrado</h1><pre>{guion}</pre>"
    except Exception as e:
        return f"Error crítico: {str(e)}"

if __name__ == '__main__':
    app.run()
