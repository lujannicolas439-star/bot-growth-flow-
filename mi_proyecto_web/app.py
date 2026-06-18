from flask import Flask, render_template_string, request

app = Flask(__name__)

# Este es el HTML con el diseño aplicado
html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white p-8 rounded-3xl shadow-2xl w-full max-w-md">
        <h1 class="text-3xl font-extrabold text-blue-900 mb-6 text-center">¡Súmate al Flow!</h1>
        <form action="/guardar" method="POST" class="space-y-4">
            <input type="text" name="cliente" placeholder="Nombre del Cliente" class="w-full p-4 rounded-xl border border-gray-200">
            <input type="text" name="producto" placeholder="Producto" class="w-full p-4 rounded-xl border border-gray-200">
            <input type="number" name="monto" placeholder="Monto ($)" class="w-full p-4 rounded-xl border border-gray-200">
            <button class="w-full bg-teal-600 text-white font-bold py-4 rounded-xl">Enviar al Bot</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True, port=8158)
