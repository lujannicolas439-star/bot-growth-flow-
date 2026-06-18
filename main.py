from flask import Flask, render_template, request
import gspread
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Si no tienes el archivo filas.html, esta línea dará error.
    # Por ahora, devolvamos un texto simple.
    return "Bot Lobo funcionando correctamente"

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo electrónico')
    
    # Aquí irá tu lógica de Google Sheets
    return f"Datos de {nombre} recibidos correctamente"

if __name__ == '__main__':
    # Render asigna automáticamente el puerto, por eso usamos os.environ.get
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
