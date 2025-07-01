
from flask import Flask, request, render_template
import json, requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1251797537002623067/97qDk77RyP3Wz1c70usLIxFoWz-URJz7rR0jn8kW_loLgLHyLfktLO9QeJHlkyznx3Qj"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.to_dict()
    with open("data.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    content = f"📥 **Pendaftaran OC Baru - Eternal SMP**\n"
    content += f"**Gamertag:** {data['gamertag']}
**Nama:** {data['nama']}\n**Ras:** {data['ras']}\n**Class:** {data['class']}\n**Job:** {data['job']}\n**Role:** {data['role']}\n"
    content += f"**Sifat:** {data['sifat']}\n**Lore:** {data['lore']}\n**Tujuan:** {data['tujuan']}"
    requests.post(WEBHOOK_URL, json={"content": content})
    return "Berhasil didaftarkan!"

if __name__ == "__main__":
    app.run()

from flask import redirect, render_template_string

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if request.form.get("password") == "eternal123":
            try:
                with open("data.json", "r") as f:
                    data = [json.loads(line) for line in f if line.strip()]
            except:
                data = []
            return render_template("hasil.html", data=data)
        else:
            return "Password salah!"
    return render_template("login.html")
