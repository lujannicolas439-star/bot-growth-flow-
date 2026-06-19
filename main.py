import os
import json
import gspread
import openai
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request

app = Flask(__name__)

# --- CONFIGURACIÓN DE APIs ---
openai.api_key = os.environ.get("OPENAI_API_KEY")

# AQUÍ ES DONDE VA TU LÍNEA:
# Esto toma el valor que configuraste en el panel de Render
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_USER = "tu_correo@gmail.com" # Puedes poner tu correo aquí o también usar una variable

# --- CONFIGURACIÓN DE GOOGLE SHEETS ---
# (Tu código de conexión aquí abajo...)
