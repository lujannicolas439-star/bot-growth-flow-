from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
import openai
import os
from flask import Flask, request

app = Flask(__name__)

# Conexión segura a OpenAI usando la variable que configuramos en Render
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/guardar', methods=['POST'])
def guardar():
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    
    # Aquí creamos el prompt con la "Mentalidad de Lobo"
    prompt = f"Actúa como el mejor cerrador de ventas de Wall Street. Escribe un mensaje persuasivo para convencer a {cliente} de comprar {producto}. Enfócate en la exclusividad y la urgencia."
    
    # Llamada a la IA
    respuesta = client.chat.completions.create(
        model="gpt-4o", # O "gpt-3.5-turbo" si prefieres
        messages=[{"role": "user", "content": prompt}]
    )
    
    guion_ventas = respuesta.choices[0].message.content
    
    # Aquí puedes añadir el código para guardar en Google Sheets y/o enviar por email
    return f"<h1>Mensaje generado para {cliente}:</h1><p>{guion_ventas}</p>"

if __name__ == '__main__':
    app.run()

