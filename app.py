import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de API (Trocar por chaves reais futuramente)
INDEED_API_KEY = "SUA_CHAVE_INDEED"
LINKEDIN_API_KEY = "SUA_CHAVE_LINKEDIN"

@app.route("/")
def home():
    return "Servidor do Jobson AI rodando!"

@app.route("/buscar_vagas", methods=["GET"])
def buscar_vagas():
    cargo = request.args.get("cargo")
    localizacao = request.args.get("localizacao")

    # Simulação de resposta (Mudar para chamadas reais depois)
    vagas_mock = [
        {"empresa": "Empresa X", "vaga": f"{cargo} - {localizacao}", "link": "https://exemplo.com/vaga1"},
        {"empresa": "Empresa Y", "vaga": f"{cargo} - {localizacao}", "link": "https://exemplo.com/vaga2"},
    ]
    
    return jsonify(vagas_mock)

if __name__ == "__main__":
    app.run(debug=True)
