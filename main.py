from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Lobo funcionando correctamente."

if __name__ == '__main__':
    app.run()

    return f"Datos de {nombre} recibidos correctamente"

if __name__ == '__main__':
    # Render asigna automáticamente el puerto, por eso usamos os.environ.get
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
