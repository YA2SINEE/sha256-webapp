from flask import Flask, request, jsonify
import hashlib
import json

app = Flask(__name__)

@app.route('/')
def home():
    # Lire les données existantes dans data.json
    try:
        with open('/data/data.json', 'r') as f:
            data_store = json.load(f)
    except FileNotFoundError:
        app.logger.error("No file found")
        data_store = []

    # Créer une réponse HTML qui affiche les données
    html_content = "<h1>Bienvenue sur l'application SHA256</h1>"
    
    if data_store:
        html_content += "<h2>Historique des hashes :</h2><ul>"
        for entry in data_store:
            html_content += f"<li>Input: {entry['input']} - Hash: {entry['hash']}</li>"
        html_content += "</ul>"
    else:
        html_content += "<p>Aucune donnée trouvée.</p>"
    
    return html_content

@app.route('/hash', methods=['POST'])
def generate_hash():
    data = request.get_json()
    string_to_hash = data['string']
    hash_object = hashlib.sha256(string_to_hash.encode())
    hash_hex = hash_object.hexdigest()

    # Lire les données existantes
    try:
        with open('/data/data.json', 'r') as f:
            data_store = json.load(f)
    except FileNotFoundError:
        data_store = []

    # Ajouter la nouvelle entrée
    data_store.append({'input': string_to_hash, 'hash': hash_hex})

    # Sauvegarder dans data.json
    with open('/data/data.json', 'w') as f:
        json.dump(data_store, f, indent=4)

    return jsonify({"input": string_to_hash, "hash": hash_hex})

@app.route('/data', methods=['GET'])
def get_data():
    try:
        with open('/data/data.json', 'r') as f:
            data_store = json.load(f)
        return jsonify(data_store)
    except FileNotFoundError:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
