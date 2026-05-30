<template>
  <div class="min-h-screen bg-slate-50/50 font-sans selection:bg-orange-100 selection:text-orange-900 p-4 sm:p-8">
    <main class="max-w-3xl mx-auto pt-10 sm:pt-20 pb-16">
      
      <div class="text-center mb-10 sm:mb-12">
        <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight mb-4">
          API Интеграция
        </h1>
        <p class="text-base sm:text-lg text-slate-500">
          Единый открытый эндпоинт для работы с транскрибацией
        </p>
      </div>

      <div class="bg-white rounded-2xl shadow-sm border border-slate-100 p-6 sm:p-8">
        <div class="flex items-center gap-3 mb-6">
          <span class="p-2 rounded-lg bg-orange-50 text-orange-500">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
            </svg>
          </span>
          <h2 class="text-xl font-bold text-slate-900">Распознавание речи</h2>
        </div>

        <p class="text-slate-600 text-sm mb-6">
          Отправьте POST-запрос с аудио или видео файлом на этот URL. На данный момент авторизация (API-ключ) не требуется.
        </p>

        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
          <div class="flex-1 flex items-center bg-slate-900 rounded-xl overflow-hidden">
            <span class="bg-green-600 text-white px-2 py-0.5 rounded text-[10px] font-bold">POST</span>
            <code class="text-slate-200 text-sm font-mono px-4 py-4 sm:py-3 truncate flex-1 block">
              https://api.scribeflowai.online/v1/transcribe
            </code>
          </div>
          
          <button 
            @click="copyLink"
            class="px-6 py-4 sm:py-3 bg-orange-500 hover:bg-orange-600 text-white text-sm font-semibold rounded-xl transition-colors shadow-sm shrink-0 flex justify-center items-center gap-2"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
            Скопировать
          </button>
        </div>
        
        <div class="mt-8 pt-6 border-t border-slate-100">
           <h3 class="text-sm font-bold text-slate-800 mb-3">Пример запроса на Python:</h3>
           <div class="relative group">
             <pre class="bg-slate-900 border border-slate-800 text-slate-300 text-sm font-mono p-5 rounded-xl overflow-x-auto"><code>import requests

url = "https://api.scribeflowai.online/v1/transcribe"
files = {"file": open("audio.mp3", "rb")}

response = requests.post(url, files=files)

print(response.json())</code></pre>
           </div>
        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import { useToast } from "vue-toastification"

const toast = useToast()
const apiUrl = "https://api.scribeflowai.online/v1/transcribe"

const copyLink = async () => {
  try {
    await navigator.clipboard.writeText(apiUrl)
    toast.success("Ссылка скопирована в буфер обмена!")
  } catch (err) {
    toast.error("Не удалось скопировать ссылку")
    console.error("Ошибка копирования: ", err)
  }
}
</script>