from flask import Flask, render_template, request

app = Flask(__name__)

# Esta ruta carga tu página (filas.html)
@app.route('/')
def index():
    return render_template('filas.html')

# Esta ruta es el "puente" que recibe los datos del formulario
@app.route('/enviar', methods=['POST'])
def enviar():
    # Captura los datos del formulario que pusimos en filas.html
    nombre = request.form['nombre']
    email = request.form['email']
    
    # Aquí es donde el "Lobo" entra en acción:
    # 1. Puedes enviar esto a una base de datos o Google Sheets
    # 2. Puedes disparar la lógica de ventas o IA
    
    print(f"Nuevo Lead: {nombre} - {email}") # Esto lo verás en los Logs de Render
    return "¡Datos recibidos correctamente! Tu solicitud está siendo procesada."

if __name__ == '__main__':
    app.run()
