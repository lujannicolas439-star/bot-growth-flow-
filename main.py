from flask import Flask, render_template, request

app = Flask(__name__)

# Esta ruta carga tu página (filas.html)
@app.route('/')
def index():
    return render_template('filas.html')

# Esta ruta es el "puente" que recibe los datos del formulario
@app.route('/enviar', methods=['POST'])
def enviar():
    # Captura los datos que el cliente puso en el formulario
    nombre = request.form['nombre']
    email = request.form['email']
    
    # Aquí puedes añadir luego la lógica para enviar a Google Sheets
    print(f"Nuevo Lead recibido: {nombre} - {email}") 
    
    return "¡Gracias! Tu solicitud ha sido enviada al Lobo."

if __name__ == '__main__':
    app.run()
