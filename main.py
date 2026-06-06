from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

MODAL_WEB_ENDPOINT_URL = "https://uchihahiro228--transcribe.modal.run"

def process_with_modal(file):
    files = {'file': (file.filename, file.stream, file.mimetype)}
    response = requests.post(MODAL_WEB_ENDPOINT_URL, files=files)
    
    if response.status_code != 200:
        raise Exception(f"Modal вернул ошибку: {response.text}")
        
    return response.json().get("transcription", "")



@app.route('/api/main', methods=['POST'])
def handle_transcription_frontend():
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify({"status": "error", "message": "Файл не выбран"}), 400

    try:
        file = request.files['file']
        print(f"Фронтенд: Отправляем файл {file.filename}...")
        clean_text = process_with_modal(file)
        return jsonify({"text": clean_text}), 200
        
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500



@app.route('/api/transcribe', methods=['POST'])
def handle_transcription_api():
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify({"success": False, "message": "Файл не передан в запросе"}), 400

    try:
        file = request.files['file']
        print(f"API: Получен публичный запрос. Обрабатываем файл {file.filename}...")
        clean_text = process_with_modal(file)
        
        return jsonify({
            "success": True,
            "filename": file.filename,
            "transcription": clean_text
        }), 200
        
    except Exception as e:
        print(f"Ошибка API: {str(e)}")
        return jsonify({"success": False, "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)