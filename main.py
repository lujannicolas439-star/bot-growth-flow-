import gspread
import json
import os
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request

app = Flask(__name__)

# Cargar credenciales desde Render
creds_json = os.environ.get('GOOGLE_CREDENTIALS')
creds_dict = json.loads(creds_json)

# Definir los alcances necesarios de forma explícita
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Conectar a la hoja (usa el nombre exacto de tu archivo)
sheet = client.open("bot-growth-flow-1").sheet1

@app.route('/guardar', methods=['POST'])
def guardar():
    try:
        data = [
            request.form.get('cliente'),
            request.form.get('producto'),
            request.form.get('monto')
        ]
        sheet.append_row(data)
        return "¡Datos enviados correctamente!", 200
    except Exception as e:
        return f"Error al guardar: {str(e)}", 500
