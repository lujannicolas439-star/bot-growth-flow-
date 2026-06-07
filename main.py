from flask import Flask, render_template, request
import gspread

app = Flask(__name__)

# Configuración de tu formulario
@app.route('/')
def index():
    return render_template('filas.html')

# Ruta que procesa los datos del formulario
@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    email = request.form['email']
    
    # Aquí irá la lógica de conexión a Google Sheets
    # registrar_en_sheet(nombre, email)
    
    return f"¡Datos de {nombre} recibidos correctamente!"

if __name__ == '__main__':
    app.run()
