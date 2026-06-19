import smtplib
from email.message import EmailMessage

# ... (todo tu código anterior de conexión a Sheets y OpenAI) ...

@app.route('/guardar', methods=['POST'])
def guardar():
    cliente = request.form.get('cliente')
    producto = request.form.get('producto')
    monto = request.form.get('monto')
    
    # 1. Guardar en Sheets
    worksheet.append_row([cliente, producto, monto])
    
    # 2. Generar guion con IA
    prompt = f"Escribe un guion de ventas persuasivo para vender {producto} a {cliente} por {monto}."
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    guion = response.choices[0].message.content
    
    # 3. Enviar email
    msg = EmailMessage()
    msg.set_content(guion)
    msg['Subject'] = f'Nuevo Guion de Ventas: {cliente}'
    msg['From'] = 'tu_correo@gmail.com'
    msg['To'] = 'tu_correo_personal@gmail.com' # Aquí recibes el guion

    # Configuración de tu cuenta para enviar (usa App Password de Gmail)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('tu_correo@gmail.com', 'tu_app_password')
        smtp.send_message(msg)
    
    # 4. Mostrar en pantalla
    return f"<h1>Trato registrado</h1><p>El guion ha sido enviado a tu correo.</p><pre>{guion}</pre>"
