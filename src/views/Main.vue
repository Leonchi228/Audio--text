<script setup>
import { ref } from 'vue'

const fileInput = ref(null)
const isDragging = ref(false)

// выбор файла через клик
const handleFileSelect = (event) => {
  const file = event.target.files[0]
  if (file) {
    processFile(file)
  }
}

//перетаскивание файла
const handleDrop = (event) => {
  isDragging.value = false
  const file = event.dataTransfer.files[0]
  if (file) {
    processFile(file)
  }
}

const isLoading = ref(false) // Создаем состояние загрузки

const processFile = async (file) => {
  isLoading.value = true // Включаем "спиннер"
  
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
    console.log('Успех!', result)
    
  } catch (error) {
    console.error('Что-то пошло не так:', error.message)
    alert('Не удалось отправить файл')
  } finally {
    isLoading.value = false 
  }
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
        <div 
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
            'p-4 rounded-full mb-4 transition-colors duration-200',
            isDragging ? 'bg-orange-100 text-orange-500' : 'bg-slate-100 text-slate-600 group-hover:bg-orange-50 group-hover:text-orange-500'
          ]">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
            </svg>
          </div>

          <h3 class="text-lg font-semibold text-slate-900 mb-1 text-center">
            Нажмите для загрузки файла
          </h3>
          <p class="text-sm text-slate-500 text-center mb-4">
            или перетащите его прямо сюда
          </p>

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
          <p class="text-sm text-slate-500 leading-relaxed max-w-xs mx-auto">
            Поддержка всех популярных аудио и видео форматов. Вам не нужно конвертировать файлы заранее.
          </p>
        </div>

        <div class="text-center flex flex-col items-center">
          <div class="w-12 h-12 flex items-center justify-center bg-slate-100 text-slate-700 rounded-xl mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <h4 class="text-base font-semibold text-slate-900 mb-2">Быстро и точно</h4>
          <p class="text-sm text-slate-500 leading-relaxed max-w-xs mx-auto">
            Высокая скорость обработки благодаря современным ИИ-моделям и отличная точность распознавания.
          </p>
        </div>

        <div class="text-center flex flex-col items-center">
          <div class="w-12 h-12 flex items-center justify-center bg-slate-100 text-slate-700 rounded-xl mb-4">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
          </div>
          <h4 class="text-base font-semibold text-slate-900 mb-2">Удобный экспорт</h4>
          <p class="text-sm text-slate-500 leading-relaxed max-w-xs mx-auto">
            Копируйте текст в буфер обмена одним кликом или скачивайте готовый файл в форматах TXT, SRT или DOCX.
          </p>
        </div>
      </div>

    </main>
  </div>
</template>

