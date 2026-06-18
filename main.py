import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuración de credenciales desde Render
creds_json = os.environ.get('GOOGLE_CREDENTIALS')
creds_dict = json.loads(creds_json)
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Conectar con tu hoja (pon el nombre exacto de tu archivo en Google Sheets)
sheet = client.open("NombreDeTuHoja").sheet1 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    
    # Escribir en la hoja
    sheet.append_row([cliente, producto, monto])
    
    return "¡Datos enviados con éxito!"

if __name__ == '__main__':
    app.run()
