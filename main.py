import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuración de credenciales
creds_json = os.environ.get('GOOGLE_CREDENTIALS')
creds_dict = json.loads(creds_json)
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Conexión a la hoja (verifica que el nombre sea el correcto en tu Google Drive)
sheet = client.open("bot-growth-flow-1").sheet1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    sheet.append_row([cliente, producto, monto])
    return "¡Enviado con éxito!", 200

if __name__ == '__main__':
    app.run()

