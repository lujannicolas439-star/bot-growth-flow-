import os
import json
import gspread
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # 1. Obtener credenciales desde las variables de entorno de Render
    creds_json = os.environ.get('GOOGLE_CREDENTIALS')
    
    if not creds_json:
        return "Error: GOOGLE_CREDENTIALS no encontrada en Render"
    
    # 2. Conectar a Google Sheets
    creds_dict = json.loads(creds_json)
    gc = gspread.service_account_from_dict(creds_dict)
    
    # 3. Abrir la hoja (asegúrate de que el nombre sea exacto)
    try:
        sh = gc.open("bot-growth-flow-1") # Nombre de tu archivo de Google Sheets
        wks = sh.sheet1
        
        # 4. Escribir datos
        wks.append_row(["Conectado", "Estado", "Operativo"])
        return "¡Bot growth from 1 conectado y escribiendo en la hoja!"
    except Exception as e:
        return f"Error al conectar con la hoja: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

