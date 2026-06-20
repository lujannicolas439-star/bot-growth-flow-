import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openai
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request

app = Flask(__name__)

# 1. CONFIGURACIÓN
openai.api_key = os.environ.get("OPENAI_API_KEY")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_USER = "lujannicolas439@gmail.com" # CAMBIA ESTO POR TU CORREO

# 2. CONEXIÓN A GOOGLE SHEETS (Sin archivos temporales)
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(os.environ.get("GOOGLE_CREDENTIALS"))
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
gc = gspread.authorize(creds)
sh = gc.open("bot-growth-flow-1")
worksheet = sh.sheet1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    try:
        cliente = request.form.get('cliente')
        producto = request.form.get('producto')
        monto = request.form.get('monto')
        
        # Guardar en Sheet
        worksheet.append_row([cliente, producto, monto])
        
        # Generar guion
        prompt = f"Escribe un guion de ventas persuasivo para vender {producto} a {cliente} por {monto}."
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        guion = response.choices[0].message.content
        
        # Enviar email
        msg = EmailMessage()
        msg.set_content(guion)
        msg['Subject'] = f'Nuevo Trato: {cliente}'
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_USER 

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        
        return "Trato registrado y email enviado."
    except Exception as e:
        return f"Error en el servidor: {str(e)}"

if __name__ == '__main__':
    app.run()
