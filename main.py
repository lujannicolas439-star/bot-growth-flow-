from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    # Aquí irá tu lógica para conectar con Google Sheets más adelante
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    print(f"Datos recibidos: {cliente}, {producto}, {monto}")
    return "Datos recibidos correctamente"

if __name__ == '__main__':
    app.run()

