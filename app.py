import modal
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# ИСПРАВЛЕНО: разрешаем запросы именно с порта Vite
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

APP_NAME = "whisper-app"
FUNCTION_NAME = "transcribe"

try:
    f = modal.Function.from_name(APP_NAME, FUNCTION_NAME)
    print("✅ Успешно подключено к Modal Whisper")
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
    f = None

@app.route('/upload', methods=['POST'])
def upload_to_modal():
    if not f:
        return jsonify({"error": "Сервис Modal не запущен. Сделай 'modal deploy'"}), 503
        
    if 'file' not in request.files:
        return jsonify({"error": "Файл не получен"}), 400
    
    file = request.files['file']
    try:
        file_bytes = file.read()
        # Вызов облачной функции
        result_text = f.remote(file_bytes) 
        
        return jsonify({
            "success": True,
            "transcription": result_text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)