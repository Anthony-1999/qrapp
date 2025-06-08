from flask import Flask, request, redirect
from datetime import datetime
import requests

app = Flask(__name__)

def obtener_info_ip(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            ciudad = data.get("city", "Desconocida")
            pais = data.get("country", "Desconocido")
            isp = data.get("org", "Desconocido")
            return ciudad, pais, isp
    except Exception:
        pass
    return "Desconocida", "Desconocido", "Desconocido"

@app.route('/')
def redirigir():
    # Obtener IP real, considerando proxies
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ',' in ip:
        ip = ip.split(',')[0].strip()

    ciudad, pais, isp = obtener_info_ip(ip)

    user_agent = request.headers.get('User-Agent', 'Desconocido')

    # Detectar dispositivo básico
    if 'Android' in user_agent:
        dispositivo = 'Android'
    elif 'iPhone' in user_agent or 'iPad' in user_agent:
        dispositivo = 'iOS'
    elif 'Windows' in user_agent:
        dispositivo = 'Windows'
    elif 'Macintosh' in user_agent:
        dispositivo = 'Mac'
    else:
        dispositivo = 'Otro'

    ahora = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs.txt", "a") as f:
        f.write(f"{ahora}, {ip}, {ciudad}, {pais}, {isp}, {dispositivo}, {user_agent}\n")

    return redirect("https://linktr.ee/Crac.UAD?utm_source=qr_code", code=302)

if __name__ == "__main__":
    app.run(debug=True)
