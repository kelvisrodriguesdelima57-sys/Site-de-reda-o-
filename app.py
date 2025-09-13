from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyBdRuoWqd7oHTF5F9C1kiN-zcWGalbN3aE"
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
                                                                                                                                                "X-goog-api-key": GEMINI_API_KEY
                                                                                                                                                    }

                                                                                                                                                        response = requests.post(API_URL, headers=headers, json=payload)

                                                                                                                                                            if response.status_code == 200:
                                                                                                                                                                    try:
                                                                                                                                                                                text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
                                                                                                                                                                                        except Exception:
                                                                                                                                                                                                    text = "Erro ao processar resposta da API"
                                                                                                                                                                                                            return jsonify({"texto": text})
                                                                                                                                                                                                                else:
                                                                                                                                                                                                                        return jsonify({"erro": response.text}), 500

                                                                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                                            app.run(debug=True)