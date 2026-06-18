import os
import json
import gspread

# 1. Cargar las credenciales desde la variable de entorno
# Render buscará la variable que guardaste en "Environment"
creds_json = os.environ.get('GOOGLE_CREDENTIALS')

if not creds_json:
    print("Error: No se encontró la variable GOOGLE_CREDENTIALS")
else:
    # 2. Convertir el texto JSON en un diccionario de Python
    creds_dict = json.loads(creds_json)
    
    # 3. Autenticación con gspread
    gc = gspread.service_account_from_dict(creds_dict)
    
    # 4. Conexión a la hoja (asegúrate de que el nombre sea exactamente "Bot_lobo")
    try:
        sh = gc.open("Bot_lobo")
        wks = sh.sheet1
        
        # 5. Prueba de conexión: escribimos una línea para confirmar
        wks.append_row(["Estado", "Bot-Lobo", "Online"])
        print("¡Éxito! El bot ha escrito en la hoja.")
    except Exception as e:
        print(f"Error al conectar con la hoja: {e}")
