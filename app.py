from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def redirigir():
    # Guarda detalles en un archivo de texto
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()}, {request.remote_addr}, {request.user_agent}\n")

    # Cambia esta URL por tu destino real
    return redirect("https://linktr.ee/Crac.UAD?utm_source=qr_code", code=302)
