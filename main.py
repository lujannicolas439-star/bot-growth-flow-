from flask import Flask, render_template
import os

# Al crear la app, Flask ya busca automáticamente en 'templates'
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

