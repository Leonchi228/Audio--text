<template>
  <div class="min-h-screen bg-slate-50/50 font-sans selection:bg-orange-100 selection:text-orange-900">
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-16">
      
      <div class="text-center max-w-2xl mx-auto mb-16">
        <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight mb-4">
          Документация и руководства
        </h1>
        <p class="text-base md:text-lg text-slate-500">
          Всё о возможностях сервиса ScribeFlow AI, правилах использования и интеграции.
        </p>
      </div>

      <div class="space-y-12">
        
        <section class="bg-white rounded-2xl shadow-sm border border-slate-100 p-6 sm:p-8">
          <h2 class="text-xl sm:text-2xl font-bold text-slate-900 mb-6 flex items-center gap-3">
            <span class="p-2 rounded-lg bg-orange-50 text-orange-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
            </span>
            Для кого этот ресурс?
          </h2>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div class="p-4 bg-slate-50 rounded-xl border border-slate-100">
              <h3 class="font-bold text-slate-900 mb-1">Блогеры и контент-мейкеры</h3>
              <p class="text-sm text-slate-600 leading-relaxed">Быстрое создание субтитров, превращение видеороликов YouTube и Reels в текстовые посты или статьи.</p>
            </div>
            <div class="p-4 bg-slate-50 rounded-xl border border-slate-100">
              <h3 class="font-bold text-slate-900 mb-1">Журналисты и копирайтеры</h3>
              <p class="text-sm text-slate-600 leading-relaxed">Расшифровка интервью, голосовых заметок, лекций и зум-созвонов без ручного набора текста.</p>
            </div>
            <div class="p-4 bg-slate-50 rounded-xl border border-slate-100">
              <h3 class="font-bold text-slate-900 mb-1">Студенты и преподаватели</h3>
              <p class="text-sm text-slate-600 leading-relaxed">Конспектирование аудиозаписей семинаров, защита курсовых, перевод диктофонных записей в текст.</p>
            </div>
            <div class="p-4 bg-slate-50 rounded-xl border border-slate-100">
              <h3 class="font-bold text-slate-900 mb-1">Разработчики</h3>
              <p class="text-sm text-slate-600 leading-relaxed">Интеграция распознавания речи Whisper в собственные приложения и автоматизация медиа-пайплайнов.</p>
            </div>
          </div>
        </section>


        <section class="bg-white rounded-2xl shadow-sm border border-slate-100 p-6 sm:p-8">
          <h2 class="text-xl sm:text-2xl font-bold text-slate-900 mb-6 flex items-center gap-3">
            <span class="p-2 rounded-lg bg-orange-50 text-orange-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122" />
              </svg>
            </span>
            Инструкция по использованию
          </h2>
          
          <div class="relative pl-6 border-l-2 border-slate-100 space-y-8">
            <div class="relative">
              <span class="absolute -left-[31px] top-0 flex items-center justify-center w-6 h-6 rounded-full bg-orange-500 text-white text-xs font-bold">1</span>
              <h3 class="font-bold text-slate-900 mb-1">Подготовьте файл</h3>
              <p class="text-sm text-slate-600">Убедитесь, что ваше аудио или видео имеет формат MP3, MP4, WAV или M4A, а его размер не превышает 1 ГБ.</p>
            </div>
            <div class="relative">
              <span class="absolute -left-[31px] top-0 flex items-center justify-center w-6 h-6 rounded-full bg-orange-500 text-white text-xs font-bold">2</span>
              <h3 class="font-bold text-slate-900 mb-1">Загрузите на сайт</h3>
              <p class="text-sm text-slate-600">Перетащите медиафайл в зону загрузки на главной странице или кликните по ней, чтобы выбрать файл на устройстве.</p>
            </div>
            <div class="relative">
              <span class="absolute -left-[31px] top-0 flex items-center justify-center w-6 h-6 rounded-full bg-orange-500 text-white text-xs font-bold">3</span>
              <h3 class="font-bold text-slate-900 mb-1">Получите и скопируйте текст</h3>
              <p class="text-sm text-slate-600">Нейросеть Whisper автоматически распознает речь. Как только обработка завершится, текст появится прямо в окне загрузки. Нажмите кнопку «Копировать».</p>
            </div>
          </div>
        </section>


        <section class="bg-white rounded-2xl shadow-sm border border-slate-100 p-6 sm:p-8">
          <h2 class="text-xl sm:text-2xl font-bold text-slate-900 mb-2 flex items-center gap-3">
            <span class="p-2 rounded-lg bg-orange-50 text-orange-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
              </svg>
            </span>
            ScribeFlow API (В разработке)
          </h2>
          <p class="text-xs text-orange-600 font-medium mb-6 bg-orange-50 inline-block px-2.5 py-1 rounded-md">Скоро появится</p>
          
          <p class="text-sm text-slate-600 leading-relaxed mb-6">
            Вы сможете автоматизировать процессы транскрибации, отправляя аудиофайлы напрямую на наши эндпоинты. Ниже представлено предварительное руководство для разработчиков.
          </p>

          <div class="mb-4">
            <h3 class="text-sm font-bold text-slate-800 mb-2">Эндпоинт транскрибации</h3>
            <div class="flex items-center gap-2 bg-slate-900 text-slate-100 text-xs font-mono p-3 rounded-xl overflow-x-auto">
              <span class="bg-green-600 text-white px-2 py-0.5 rounded text-[10px] font-bold">POST</span>
              <span>https://api.scribeflowai.online/v1/transcribe</span>
            </div>
          </div>

          <div>
            <h3 class="text-sm font-bold text-slate-800 mb-2">Пример запроса на Python</h3>
            <pre class="bg-slate-900 text-slate-200 text-xs font-mono p-4 rounded-xl overflow-x-auto"><code>import requests

url = "https://api.scribeflowai.online/v1/transcribe"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
files = {
    "file": open("audio.mp3", "rb")
}

response = requests.post(url, headers=headers, files=files)
print(response.json())</code></pre>
          </div>

          <div class="mt-4">
            <h3 class="text-sm font-bold text-slate-800 mb-2">Пример успешного ответа (JSON)</h3>
            <pre class="bg-slate-900 text-slate-200 text-xs font-mono p-4 rounded-xl overflow-x-auto"><code>{
  "success": true,
  "filename": "audio.mp3",
  "transcription": "Текст, который успешно распознала нейросеть Whisper..."
}</code></pre>
          </div>
        </section>

      </div>
      
    </main>
  </div>
</template>

<script setup>

</script>