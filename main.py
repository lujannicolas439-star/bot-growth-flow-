from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza el archivo index.html que está en la carpeta templates
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    # Aquí irá tu lógica de Google Sheets más adelante
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    return f"Datos recibidos: {cliente}, {producto}, {monto}"

if __name__ == '__main__':
    app.run()
