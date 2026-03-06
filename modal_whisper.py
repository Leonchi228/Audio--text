import modal
import os

image = (
    modal.Image.debian_slim()
    .apt_install("ffmpeg")
    .pip_install("openai-whisper")
)

app = modal.App("whisper-app", image=image) 

@app.function(
    gpu="any",
    timeout=600,
)
def transcribe(file_bytes: bytes):
    import whisper
    import tempfile
    import os
    import re

    model = whisper.load_model("large-v3") 

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(file_bytes)
        temp_path = temp_file.name

    try:
        # Оставляем строгие настройки для точности
        result = model.transcribe(
            temp_path, 
            language="ru", 
            temperature=0,
            initial_prompt="Транскрибация учебного курса. Без лишних фраз в конце."
        )
        
        text = result["text"].strip()

        # Список "черных" фраз, которые Whisper любит выдумывать в тишине
        hallucinations = [
            "Продолжение следует",
            "Продолжение следует...",
            "Подписывайтесь на канал",
            "Подпишитесь на мой канал",
            "Ставьте лайки",
            "Спасибо за просмотр",
            "To be continued",
            "Subtitles by",
            "Текст подготовил",
            "Перевод"
        ]

        # Очистка текста: удаляем эти фразы, если они стоят в самом конце или начале
        for phrase in hallucinations:
            # Используем регулярное выражение, чтобы удалять фразу без учета регистра
            # и лишних знаков препинания в конце
            pattern = re.compile(re.escape(phrase), re.IGNORECASE)
            text = pattern.sub("", text)

        return text.strip()

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)