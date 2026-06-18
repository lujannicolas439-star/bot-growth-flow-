import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request

app = Flask(__name__)

# 1. Configuración de seguridad: lee el JSON desde la variable de entorno de Render
creds_json = os.environ.get('GOOGLE_CREDENTIALS')
creds_dict = json.loads(creds_json)

# 2. Autenticación
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# 3. Conexión con tu hoja (¡Asegúrate que el nombre aquí sea EXACTAMENTE igual al de tu archivo en Google Drive!)
sheet = client.open("bot-growth-flow-1").sheet1 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    # Captura los datos del formulario
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    
    # Escribe en la hoja de cálculo
    sheet.append_row([cliente, producto, monto])
    
    return "¡Datos enviados correctamente! Ya puedes cerrar esta pestaña."

if __name__ == '__main__':
    app.run()
