from flask import Flask, render_template

app = Flask(__name__)

# Esta es la ruta que le dice al servidor qué mostrar al entrar
@app.route('/')
def home():
    return render_template('index.html')

