from flask import Flask, render_template, request
import os
import openai

# 1. PRIMERO definimos la aplicación
app = Flask(__name__)

# 2. LUEGO configuramos la clave de la IA
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 3. AHORA definimos la ruta del formulario
@app.route('/')
def home():
    return render_template('index.html')

# 4. Y finalmente la ruta para procesar el formulario
@app.route('/guardar', methods=['POST'])
def guardar():
    # Aquí irá tu lógica de ventas
    return "¡Trato procesado!"

# 5. Esto es necesario para que Flask arranque
if __name__ == '__main__':
    app.run()
