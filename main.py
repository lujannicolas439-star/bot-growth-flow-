import os
import json
import gspread
import openai
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request

app = Flask(__name__)

# 1. CONFIGURACIÓN DE APIs (Render toma esto de las Variables de Entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_USER = "lujanicolas439@gmail.com"  # CAMBIA ESTO POR TU CORREO REAL

# 2. CONFIGURACIÓN GOOGLE SHEETS
# Crea el archivo temporal para las credenciales
creds_dict = json.loads(os.environ.get("GOOGLE_CREDENTIALS"))
with open('creds.json', 'w') as f:
    json.dump(creds_dict, f)

gc = gspread.service_account(filename='creds.json')
sh = gc.open("bot-growth-flow-1")
worksheet = sh.sheet1

# 3. RUTAS
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    # Obtener datos del formulario
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    
    # Guardar en Sheet
    worksheet.append_row([cliente, producto, monto])
    
    # Generar guion con IA
    prompt = f"Escribe un guion de ventas persuasivo para vender {producto} a {cliente} por {monto}."
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    guion = response.choices[0].message.content
    
    # Enviar email
    msg = EmailMessage()
    msg.set_content(guion)
    msg['Subject'] = f'Nuevo Guion de Ventas: {cliente}'
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER 

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASSWORD)
        smtp.send_message(msg)
    
    return f"<h1>Trato registrado</h1><p>El guion fue enviado a tu correo.</p><pre>{guion}</pre>"

if __name__ == '__main__':
    app.run()
