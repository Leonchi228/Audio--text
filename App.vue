<script setup>
import { ref } from 'vue'
import Header from './Header.vue'

// Состояния
const file = ref(null)
const transcription = ref('') 
const isLoading = ref(false)
const isDragging = ref(false)
const progress = ref(0)
const error = ref('')
const showCopyTooltip = ref(false)

// Обработка выбора файла
const handleFile = (selectedFile) => {
  if (!selectedFile) return
  // Простая проверка: если это видео, Modal на бэкенде сам извлечет аудио через ffmpeg
  file.value = selectedFile
  transcription.value = '' 
  error.value = ''
}

const onDrop = (e) => {
  isDragging.value = false
  const droppedFile = e.dataTransfer.files[0]
  handleFile(droppedFile)
}

// Отправка на сервер
const sendToWhisper = async () => {
  if (!file.value) return
  
  isLoading.value = true
  progress.value = 10
  error.value = ''
  
  const formData = new FormData()
  formData.append('file', file.value)

  try {
    // Имитация движения прогресс-бара
    const interval = setInterval(() => {
      if (progress.value < 90) progress.value += 5
    }, 500)

    const response = await fetch('http://127.0.0.1:5000/upload', {
      method: 'POST',
      body: formData
    })
    
    clearInterval(interval)
    progress.value = 100

    if (!response.ok) throw new Error('Ошибка сервера (проверьте Flask)')

    const data = await response.json()
    
    if (data.success) {
      transcription.value = data.transcription
    } else {
      error.value = data.error || 'Ошибка обработки'
    }
  } catch (err) {
    error.value = 'Сервер Flask не отвечает. Убедитесь, что он запущен на порту 5000.'
  } finally {
    setTimeout(() => {
      isLoading.value = false
      progress.value = 0
    }, 400)
  }
}

// Копирование текста
const copyText = () => {
  if (!transcription.value) return
  navigator.clipboard.writeText(transcription.value)
  
  showCopyTooltip.value = true
  setTimeout(() => {
    showCopyTooltip.value = false
  }, 2000)
}

// Сброс для новой загрузки
const resetAll = () => {
  file.value = null
  transcription.value = ''
  error.value = ''
}
</script>

<template>
  <Header />
  
  <main class="main-content">
    <div class="container main-container">
      
      <template v-if="!transcription && !isLoading">
        <h1 class="main-title">Конвертер аудио и видео в текст</h1>
        <p class="main-subtitle">
          Перетащите файл в область ниже, чтобы начать мгновенную транскрибацию.<br>
          Мы сами извлечем звук из вашего видео.
        </p>
      </template>

      <div 
        v-if="!transcription && !isLoading" 
        class="upload-area" 
        :class="{ 'dragging': isDragging, 'file-selected': file }"
        @dragover.prevent="isDragging = true"
        @dragleave.prevent="isDragging = false"
        @drop.prevent="onDrop"
      >
        <div class="upload-icon">
          <svg v-if="!file" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
          <svg v-else width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="2">
            <polyline points="20 6 9 17 4 12"></polyline></svg>
        </div>

        <p class="upload-text">{{ file ? file.name : 'Нажмите или перетащите файл' }}</p>
        <p class="upload-subtext">MP3, WAV, MP4, MOV и другие</p>
        <input type="file" @change="(e) => handleFile(e.target.files[0])" accept="audio/*,video/*" class="file-input" />
      </div>

      <div v-if="isLoading" class="progress-wrapper">
        <p class="loading-status">Нейросеть Whisper обрабатывает ваш файл...</p>
        <div class="progress-container">
          <div class="progress-fill" :style="{ width: progress + '%' }"></div>
        </div>
      </div>

      <button 
        v-if="file && !transcription && !isLoading" 
        @click="sendToWhisper" 
        class="action-btn"
      >
        Начать транскрибацию
      </button>

      <div v-if="transcription" class="result-box">
        <div class="result-header">
          <h3>Результат транскрибации</h3>
          <button @click="resetAll" class="reset-btn">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
            Новый файл
          </button>
        </div>

        <div class="textarea-wrapper">
          <button @click="copyText" class="copy-icon-btn" :class="{ 'copied': showCopyTooltip }">
            <span v-if="showCopyTooltip" class="copy-tooltip">Скопировано!</span>
            <svg v-if="!showCopyTooltip" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
              <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="2">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </button>

          <textarea v-model="transcription" class="result-text" readonly></textarea>
        </div>
      </div>
      
      <p v-if="error" class="error-msg">{{ error }}</p>
    </div>
  </main>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.main-content {
  padding-top: 120px;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  background-color: #ffffff;
  font-family: 'Inter', sans-serif;
}

.main-container {
  width: 100%;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 20px;
}

.main-title { font-size: 2.5rem; font-weight: 800; color: #0a0a0f; margin-bottom: 12px; }
.main-subtitle { color: #718096; font-size: 1.1rem; margin-bottom: 40px; line-height: 1.6; text-align: center; }

/* Upload Area */
.upload-area {
  width: 100%;
  max-width: 600px;
  padding: 60px 40px;
  border: 1px solid #f0f0f0;
  background-color: #fafafa;
  border-radius: 20px;
  position: relative;
  transition: all 0.3s ease;
  cursor: pointer;
}

.upload-area.dragging { border: 2px solid #0a0a0f; background-color: #f7fafc; transform: scale(1.01); }
.upload-area.file-selected { border-color: #2ecc71; background-color: #fafffa; }

.upload-icon { margin-bottom: 20px; color: #718096; }
.upload-text { font-weight: 600; color: #1a202c; font-size: 1.1rem; margin-bottom: 6px; }
.upload-subtext { font-size: 0.85rem; color: #a0aec0; }
.file-input { position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; cursor: pointer; }

/* Progress Bar */
.progress-wrapper { width: 100%; max-width: 600px; margin-top: 50px; }
.loading-status { font-size: 0.95rem; color: #4a5568; margin-bottom: 12px; font-weight: 500; }
.progress-container { width: 100%; height: 6px; background: #f0f0f0; border-radius: 10px; overflow: hidden; }
.progress-fill { height: 100%; background: #0a0a0f; transition: width 0.4s ease; }

/* Action Button */
.action-btn {
  margin-top: 30px;
  background-color: #0a0a0f;
  color: white;
  border: none;
  padding: 14px 40px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 1rem;
  cursor: pointer;
  transition: opacity 0.2s;
}

.action-btn:hover { opacity: 0.9; }

/* Result Box */
.result-box { width: 100%; animation: slideUp 0.5s ease-out; }
.result-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.result-header h3 { font-size: 1.2rem; font-weight: 800; color: #1a202c; }

.textarea-wrapper { position: relative; width: 100%; }
.result-text {
  width: 100%; height: 400px; padding: 25px; padding-top: 50px;
  border: 1px solid #f0f0f0; border-radius: 16px; background: #ffffff;
  font-size: 1.05rem; line-height: 1.8; color: #2d3748; outline: none; resize: vertical;
}

/* Copy Button */
.copy-icon-btn {
  position: absolute; top: 15px; right: 15px;
  background: white; border: 1px solid #edf2f7; border-radius: 8px;
  padding: 8px; cursor: pointer; transition: all 0.2s; z-index: 5;
}
.copy-icon-btn:hover { border-color: #cbd5e1; background: #f7fafc; }
.copy-tooltip {
  position: absolute; right: 45px; top: 8px;
  background: #1a202c; color: white; font-size: 12px;
  padding: 5px 10px; border-radius: 6px; white-space: nowrap;
}

.reset-btn {
  background: none; border: none; color: #718096;
  font-size: 0.9rem; font-weight: 600; cursor: pointer;
  display: flex; align-items: center; gap: 8px;
}

@keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.error-msg { color: #e53e3e; margin-top: 20px; font-weight: 500; }
</style>