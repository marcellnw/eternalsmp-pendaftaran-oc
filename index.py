
from flask import Flask, request, render_template
import json, os, requests

app = Flask(__name__, static_folder="static", template_folder="templates")

WEBHOOK_URL = "https://discord.com/api/webhooks/1251797537002623067/97qDk77RyP3Wz1c70usLIxFoWz-URJz7rR0jn8kW_loLgLHyLfktLO9QeJHlkyznx3Qj"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hasil")
def hasil():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        data = []
    return render_template("hasil.html", data=data)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.to_dict()
    payload = {
        "content": "**Pendaftaran OC Baru - Eternal SMP Season 14**\n"
                   f"**Gamertag:** {data.get('gamertag')}\n"
                   f"**Nama:** {data.get('nama')}\n"
                   f"**Ras:** {data.get('ras')}\n"
                   f"**Class:** {data.get('class')}\n"
                   f"**Job:** {data.get('job')}\n"
                   f"**Sifat:** {data.get('sifat')}\n"
                   f"**Lore:** {data.get('lore')}\n"
                   f"**Tujuan:** {data.get('tujuan')}\n"
                   f"**Role:** {data.get('role')}"
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except:
        pass
    try:
        with open("data.json", "r") as f:
            all_data = json.load(f)
    except:
        all_data = []
    all_data.append(data)
    with open("data.json", "w") as f:
        json.dump(all_data, f, indent=2)
    return "Pendaftaran berhasil!"

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
