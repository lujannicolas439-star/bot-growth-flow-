import gspread
from flask import request

# Configura la conexión (esto debe ir fuera de la función, al inicio)
gc = gspread.service_account(filename='credentials.json')
sh = gc.open("bot-growth-flow-1") # Asegúrate que el nombre coincida
worksheet = sh.sheet1

@app.route('/guardar', methods=['POST'])
def guardar():
    # Obtener datos del formulario
    empresa = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    
    # Escribir en la hoja
    worksheet.append_row([empresa, producto, monto])
    
    return "¡Trato guardado exitosamente en la hoja!"
