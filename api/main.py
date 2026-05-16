from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


MODAL_WEB_ENDPOINT_URL = "https://uchihahiro228--transcribe.modal.run"

@app.route('/api/main', methods=['POST'])
def handle_transcription():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "Файл не найден в запросе"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "Файл не выбран"}), 400

    try:
        print(f"Файл {file.filename} получен. Пересылаю напрямую в Modal веб-эндпоинт...")

        files = {
            'file': (file.filename, file.stream, file.mimetype)
        }
        
        # Делаем прямой POST-запрос к твоей нейросети
        response = requests.post(MODAL_WEB_ENDPOINT_URL, files=files)
        
        if response.status_code != 200:
            print(f"Modal вернул ошибку: {response.text}")
            return jsonify({"status": "error", "message": "Ошибка на стороне нейросети"}), response.status_code

        modal_data = response.json()

        clean_text = modal_data.get("transcription", "")
        

        return jsonify({"text": clean_text}), 200

    except Exception as e:
        print(f"Исключение на бэкенде Flask: {str(e)}")
        return jsonify({"status": "error", "message": f"Ошибка транзита: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)