<script setup>
import { ref } from 'vue'
import { supabase } from '../supabase' 

const fileInput = ref(null)
const isDragging = ref(false)
const isLoading = ref(false)

// Переменные для хранения результата
const resultText = ref('')
const uploadedFileName = ref('')

const handleFileSelect = (event) => {
  const file = event.target.files[0]
  if (file) processFile(file)
}

const handleDrop = (event) => {
  isDragging.value = false
  const file = event.dataTransfer.files[0]
  if (file) processFile(file)
}

const processFile = async (file) => {
  isLoading.value = true 
  resultText.value = '' 
  uploadedFileName.value = file.name
  
  try {
    const formData = new FormData()
    formData.append('file', file)

    const response = await fetch('http://127.0.0.1:5000/api/main', {
      method: 'POST',
      body: formData
    })

    if (!response.ok) {
      throw new Error('Ошибка сервера: ' + response.status)
    }

    const result = await response.json()
    resultText.value = result.text // Записываем текст для вывода

  } catch (error) {
    console.error('Ошибка:', error.message)
    alert(error.message || 'Не удалось обработать файл')
  } finally {
    isLoading.value = false 
  }

  // Фоновое сохранение в базу данных Supabase
  try {
    const { data: { session } } = await supabase.auth.getSession()
    if (session && resultText.value) {
      await supabase.from('transcriptions').insert([
        {
          user_id: session.user.id,
          title: uploadedFileName.value,
          content: resultText.value
        }
      ])
      console.log('Успешно сохранено в Supabase!')
    }
  } catch (dbError) {
    console.error('Ошибка Supabase:', dbError.message)
  }
}

// Сброс состояния для загрузки нового файла
const resetUploader = () => {
  resultText.value = ''
  uploadedFileName.value = ''
  if (fileInput.value) fileInput.value.value = ''
}

const copyToClipboard = () => {
  navigator.clipboard.writeText(resultText.value)
  alert('Текст скопирован в буфер обмена!')
}
</script>

<template>
  <div class="min-h-screen bg-slate-50/50 font-sans selection:bg-orange-100 selection:text-orange-900">
    <main class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-16">
      
      <div class="text-center max-w-2xl mx-auto mb-12">
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
          Конвертер аудио и видео в текст
        </h1>
        <p class="text-base md:text-lg text-slate-500 leading-relaxed">
          Преобразуйте ваши аудио и видео файлы в текст за считанные минуты. <br class="hidden md:block" />
          Идеально подходит для блогеров, видеомейкеров и копирайтеров.
        </p>
      </div>

      <div class="max-w-3xl mx-auto bg-white rounded-2xl shadow-sm border border-slate-100 p-4 sm:p-8 mb-16">
        
        <div v-if="isLoading" class="flex flex-col items-center justify-center py-20 px-4">
          <svg class="animate-spin h-12 w-12 text-orange-500 mb-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <h3 class="text-lg font-semibold text-slate-900 mb-1 text-center">Идет расшифровка...</h3>
          <p class="text-sm text-slate-500 text-center max-w-xs">Пожалуйста, не закрывайте вкладку. Нейросеть обрабатывает файл.</p>
        </div>

        <div v-else-if="resultText" class="animate-fade-in">
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 pb-4 border-b border-slate-100 mb-4">
            <div class="truncate max-w-xs sm:max-w-md">
              <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-green-500"></span>
                Текст успешно распознан
              </h3>
              <p class="text-xs text-slate-400 mt-0.5 truncate">{{ uploadedFileName }}</p>
            </div>
            
            <div class="flex w-full sm:w-auto gap-2">
              <button 
                @click="copyToClipboard"
                class="flex-1 sm:flex-initial text-xs bg-orange-500 hover:bg-orange-600 text-white px-4 py-2 rounded-lg font-medium transition-colors flex items-center justify-center gap-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                </svg>
                Копировать
              </button>
              <button 
                @click="resetUploader"
                class="flex-1 sm:flex-initial text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 px-4 py-2 rounded-lg font-medium transition-colors"
              >
                Новый файл
              </button>
            </div>
          </div>
          
          <div class="bg-slate-50 rounded-xl p-5 border border-slate-100 max-h-[400px] overflow-y-auto">
            <p class="text-sm text-slate-700 leading-relaxed whitespace-pre-line select-text">
              {{ resultText }}
            </p>
          </div>
        </div>

        <div 
          v-else
          @dragover.prevent="isDragging = true"
          @dragleave.prevent="isDragging = false"
          @drop.prevent="handleDrop"
          :class="[
            'relative flex flex-col items-center justify-center w-full py-16 px-4 border-2 border-dashed rounded-xl transition-all duration-200 group cursor-pointer',
            isDragging ? 'border-orange-400 bg-orange-50/50' : 'border-slate-200 hover:border-orange-300 hover:bg-slate-50'
          ]"
          @click="$refs.fileInput.click()"
        >
          <div :class="[
            'p-4 rounded-full mb-4 transition-colors duration-200 bg-slate-100 text-slate-600 group-hover:bg-orange-50 group-hover:text-orange-500',
            isDragging ? 'bg-orange-100 text-orange-500' : ''
          ]">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
            </svg>
          </div>

          <h3 class="text-lg font-semibold text-slate-900 mb-1 text-center">Нажмите для загрузки файла</h3>
          <p class="text-sm text-slate-500 text-center mb-4">или перетащите его прямо сюда</p>

          <div class="flex flex-wrap justify-center gap-2 mt-2">
            <span class="px-2.5 py-1 bg-slate-100 text-slate-600 rounded-md text-xs font-medium">MP3, MP4, WAV, M4A</span>
            <span class="px-2.5 py-1 bg-slate-100 text-slate-600 rounded-md text-xs font-medium">До 1 ГБ</span>
          </div>

          <input 
            type="file" 
            ref="fileInput" 
            class="hidden" 
            accept="audio/*,video/*"
            @change="handleFileSelect"
          >
        </div>

      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-12 max-w-4xl mx-auto">
        <div class="text-center flex flex-col items-center">
          <div class="w-12 h-12 flex items-center justify-center bg-slate-100 text-slate-700 rounded-xl mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3" />
            </svg>
          </div>
          <h4 class="text-base font-semibold text-slate-900 mb-2">Любые форматы</h4>
          <p class="text-sm text-slate-500 leading-relaxed max-w-xs mx-auto">Поддержка всех популярных аудио и видео форматов.</p>
        </div>

        <div class="text-center flex flex-col items-center">
          <div class="w-12 h-12 flex items-center justify-center bg-slate-100 text-slate-700 rounded-xl mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h4 class="text-base font-semibold text-slate-900 mb-2">Быстро и точно</h4>
          <p class="text-sm text-slate-500 leading-relaxed max-w-xs mx-auto">Высокая скорость обработки благодаря современным ИИ-моделям.</p>
        </div>

        <div class="text-center flex flex-col items-center">
          <div class="w-12 h-12 flex items-center justify-center bg-slate-100 text-slate-700 rounded-xl mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          </div>
          <h4 class="text-base font-semibold text-slate-900 mb-2">Удобный экспорт</h4>
          <p class="text-sm text-slate-500 leading-relaxed max-w-xs mx-auto">Копируйте текст в буфер обмена одним кликом.</p>
        </div>
      </div>

    </main>
  </div>
</template>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.25s ease-out forwards;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>