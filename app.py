from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gerar_redacao", methods=["POST"])
def gerar_redacao():
    data = request.get_json()
    tema = data.get("tema", "Tema não informado")
    pontos = data.get("pontos", [])
    tom = data.get("tom", "formal")

    prompt = f"""
Escreva uma redação no estilo ENEM sobre o tema "{tema}".
Pontos principais: {', '.join(pontos)}.
Tom: {tom}.
Inclua introdução, desenvolvimento e conclusão com proposta de intervenção.
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GOOGLE_API_KEY
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=15)
    except Exception as e:
        return jsonify({"erro": f"Falha na requisição: {str(e)}"}), 500

    # Debug completo
    try:
        resp_json = response.json()
    except Exception:
        resp_json = response.text

    if response.status_code == 200:
        try:
            text = resp_json["candidates"][0]["content"]["parts"][0]["text"]
            return jsonify({"texto": text})
        except Exception:
            return jsonify({"erro": "Não foi possível extrair o texto da resposta", "resposta_bruta": resp_json})
    else:
        return jsonify({
            "erro": "Erro na API do Gemini",
            "status_code": response.status_code,
            "resposta_bruta": resp_json
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
