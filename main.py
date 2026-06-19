import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuración de seguridad: lee el JSON desde la variable de entorno en Render
creds_json = os.environ.get('GOOGLE_CREDENTIALS')
creds_dict = json.loads(creds_json)

# Autenticación con Google
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Conexión con tu hoja (¡Asegúrate que este nombre sea exacto al de tu archivo en Drive!)
sheet = client.open("bot-growth-flow-1").sheet1 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    
    # Escribir en la hoja de cálculo
    sheet.append_row([cliente, producto, monto])
    
    return "¡Datos enviados correctamente!"

if __name__ == '__main__':
    app.run()
