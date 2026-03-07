import modal
import os
import tempfile
from fastapi import UploadFile, File, HTTPException

# 1. Создаем приложение
app = modal.App("whisper-app")

# 2. ИСПРАВЛЕННЫЙ ОБРАЗ: добавляем fastapi и python-multipart
image = (
    modal.Image.debian_slim()
    .apt_install("ffmpeg")
    .pip_install(
        "openai-whisper", 
        "ffmpeg-python", 
        "fastapi[standard]",  # Добавили это по требованию ошибки
        "python-multipart"   # Это нужно для загрузки файлов через форму
    )
)

@app.function(
    gpu="any", 
    image=image,
    timeout=600
)
@modal.web_endpoint(method="POST", label="transcribe")
async def transcribe(file: UploadFile = File(...)):
    import whisper

    # Получаем расширение (теперь поддерживает и видео, и аудио)
    suffix = os.path.splitext(file.filename)[1].lower()
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_path = temp_file.name

    try:
        # Для видео/аудио используем модель base (золотая середина скорости и качества)
        model = whisper.load_model("base")
        result = model.transcribe(temp_path)
        
        return {
            "success": True,
            "transcription": result["text"]
        }

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Ошибка обработки файла")
    
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)