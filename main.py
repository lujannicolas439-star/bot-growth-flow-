import os
import json
import gspread
import openai
from flask import Flask, render_template, request

app = Flask(__name__)

# 1. Configuración de APIs
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 2. Configuración de Google Sheets
# Cargamos las credenciales desde la variable de entorno
creds_dict = json.loads(os.environ.get("GOOGLE_CREDENTIALS"))
# Creamos un archivo temporal para que gspread lo pueda leer
with open('creds.json', 'w') as f:
    json.dump(creds_dict, f)

gc = gspread.service_account(filename='creds.json')
sh = gc.open("bot-growth-flow-1") # Asegúrate que este nombre sea exacto al de tu hoja
worksheet = sh.sheet1

# 3. Rutas
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    # Recibir datos
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    
    # Escribir en Google Sheets
    worksheet.append_row([cliente, producto, monto])
    
    # Aquí puedes añadir la llamada a OpenAI si deseas mostrar una respuesta personalizada
    return f"<h1>Trato registrado para {cliente}</h1><p>Los datos han sido guardados en el sistema.</p>"

if __name__ == '__main__':
    app.run()
