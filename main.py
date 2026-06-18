from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Esto es lo que falta: debe apuntar a tu archivo Index.html
    return render_template('Index.html')
