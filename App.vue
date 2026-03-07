<template>
  <div class="app-container">
    <header class="header">
      <h1>Whisper Audio & Video</h1>
      <p class="subtitle">Мгновенная расшифровка нейросетью</p>
    </header>

    <main class="main-content">
      <div v-if="!isProcessing && !resultText" class="upload-card">
        <div class="drop-zone">
          <input 
            type="file" 
            @change="handleFileUpload" 
            accept="audio/*,video/*" 
            id="file-input"
          />
          <label for="file-input" class="file-label">
            <span v-if="!selectedFile">Выберите аудио или видео файл</span>
            <span v-else>Выбран файл: {{ selectedFile.name }}</span>
          </label>
        </div>
        
        <button 
          @click="startTranscription" 
          :disabled="!selectedFile" 
          class="submit-btn"
        >
          Начать расшифровку
        </button>
      </div>

      <div v-if="isProcessing" class="loading-state">
        <div class="loader"></div>
        <h2>Идет обработка...</h2>
        <p>Нейросеть Whisper анализирует ваш файл. Обычно это занимает от 30 до 90 секунд.</p>
        
        <div class="ad-block">
          <p>Здесь будет реклама во время ожидания</p>
        </div>
      </div>

      <div v-if="resultText" class="result-card">
        <h3>Результат расшифровки:</h3>
        <div class="result-box">
          {{ resultText }}
        </div>
        <div class="actions">
          <button @click="copyToClipboard" class="secondary-btn">Копировать текст</button>
          <button @click="reset" class="primary-btn">Загрузить новый файл</button>
        </div>
      </div>
    </main>

    <footer class="footer">
      <div class="footer-links">
        <router-link to="/privacy">Политика конфиденциальности</router-link>
        <span class="sep">|</span>
        <a href="mailto:support@example.com">Поддержка</a>
      </div>
      <p class="copy">&copy; 2024 WhisperText. Все права защищены.</p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const selectedFile = ref(null);
const isProcessing = ref(false);
const resultText = ref(null);

// ТВОЯ НОВАЯ ССЫЛКА (Modal автоматически добавляет /transcribe в конец из-за label)
const API_URL = "https://uchihahiro228--transcribe.modal.run";

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file && file.size > 50 * 1024 * 1024) { // Лимит 50МБ
    alert("Файл слишком большой. Максимум 50 МБ.");
    return;
  }
  selectedFile.value = file;
};

const startTranscription = async () => {
  if (!selectedFile.value) return;

  isProcessing.value = true;
  resultText.value = null;

  const formData = new FormData();
  formData.append('file', selectedFile.value);

  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) throw new Error('Ошибка сервера');

    const data = await response.json();
    
    // В твоем бэкенде Modal поле называется "transcription"
    if (data.success) {
      resultText.value = data.transcription;
    } else {
      alert("Ошибка: " + data.error);
    }
  } catch (error) {
    console.error(error);
    alert("Не удалось связаться с сервером. Проверьте Modal.");
  } finally {
    isProcessing.value = false;
  }
};

const copyToClipboard = () => {
  navigator.clipboard.writeText(resultText.value);
  alert("Текст скопирован!");
};

const reset = () => {
  selectedFile.value = null;
  resultText.value = null;
};
</script>

<style scoped>
/* Добавь эти стили, чтобы всё выглядело аккуратно */
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: 'Inter', sans-serif;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
.header { text-align: center; margin-bottom: 40px; }
.upload-card, .result-card, .loading-state {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  text-align: center;
}
.drop-zone {
  border: 2px dashed #ddd;
  padding: 40px;
  margin-bottom: 20px;
  border-radius: 8px;
}
#file-input { display: none; }
.file-label { cursor: pointer; color: #42b983; font-weight: bold; }
.submit-btn {
  background: #42b983;
  color: white;
  border: none;
  padding: 12px 30px;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
}
.submit-btn:disabled { background: #ccc; }
.result-box {
  background: #f4f4f4;
  padding: 20px;
  border-radius: 8px;
  text-align: left;
  margin: 20px 0;
  white-space: pre-wrap;
}
.ad-block {
  margin-top: 20px;
  padding: 20px;
  background: #fffbe6;
  border: 1px solid #ffe58f;
  min-height: 200px;
}
.footer {
  margin-top: auto;
  padding: 40px 0 20px;
  text-align: center;
  font-size: 14px;
  color: #888;
}
.footer-links a { color: #42b983; text-decoration: none; }
.sep { margin: 0 10px; }
.loader {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #42b983;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 2s linear infinite;
  margin: 0 auto 20px;
}
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
</style>