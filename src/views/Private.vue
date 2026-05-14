<template>
  <div class="min-h-screen bg-gray-50/50 pb-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="flex justify-between items-center mb-8">
        <div>
          <h1 class="text-2xl font-bold text-[#0B132B]">Мои транскрибации</h1>
          <p class="text-sm text-gray-500 mt-1">Всего обработано: {{ transcriptions.length }} файлов</p>
        </div>
        <button class="bg-[#0F172A] text-white px-5 py-2.5 rounded-lg text-sm font-medium hover:bg-slate-800 transition-all flex items-center gap-2">
          <span>+</span> Новая транскрибация
        </button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="item in transcriptions" 
          :key="item.id" 
          class="bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow flex flex-col h-full"
        >
          <div class="mb-4">
            <h3 class="font-semibold text-[#0B132B] truncate" :title="item.title">
              {{ item.title }}
            </h3>
            <span class="text-xs text-gray-400">{{ item.date }}</span>
          </div>

          <div class="flex-grow">
            <p class="text-sm text-gray-600 leading-relaxed line-clamp-5 mb-6">
              {{ item.content }}
            </p>
          </div>

          <div class="flex items-center justify-between pt-4 border-t border-gray-100 mt-auto">
            <div class="flex gap-2">
              <button 
                @click="view(item.id)"
                class="text-xs font-medium text-[#0F172A] hover:bg-slate-50 px-3 py-1.5 rounded-md border border-gray-200 transition-colors"
              >
                Просмотреть
              </button>
              <button 
                @click="edit(item.id)"
                class="text-xs font-medium text-gray-600 hover:bg-slate-50 px-3 py-1.5 rounded-md border border-gray-200 transition-colors"
              >
                Изменить
              </button>
            </div>
            
            <button 
              @click="remove(item.id)"
              class="text-xs font-medium text-red-500 hover:bg-red-50 px-3 py-1.5 rounded-md transition-colors"
            >
              Удалить
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useToast } from "vue-toastification"
import ConfirmAction from "@/components/ConfirmAction.vue"

const transcriptions = ref([
  {
    id: 1,
    title: "Интервью с разработчиком.mp4",
    date: "03.04.2026, 14:20",
    content: "Всем привет! Сегодня мы обсуждаем будущее веб-разработки и использование искусственного интеллекта в повседневных задачах. На самом деле, нейросети уже давно помогают нам писать код, но теперь они берутся и за обработку медиаконтента. В этом выпуске мы разберем, как работают современные сервисы транскрибации и почему это важно для бизнеса. Мы пригласили эксперта из компании, которая занимается нейронными сетями уже более пяти лет..."
  },
  {
    id: 2,
    title: "Лекция по экономике #4.mp3",
    date: "02.04.2026, 10:15",
    content: "Тема сегодняшней лекции — инфляция и её влияние на покупательную способность населения. Мы рассмотрим основные виды инфляции: ползучую, галопирующую и гиперинфляцию. Обратите внимание на графики на слайдах. Важно понимать, что умеренная инфляция считается нормальным явлением для развивающейся экономики, так как она стимулирует инвестиции. Однако, когда темпы роста цен выходят из-под контроля, начинаются структурные проблемы в финансовой системе страны..."
  },
  {
    id: 3,
    title: "Встреча по Scribeflow AI.wav",
    date: "01.04.2026, 18:00",
    content: "Нужно обсудить внедрение Resend для уведомлений о сбросе пароля. Также необходимо проверить, как работает Email Enumeration Protection в настройках Supabase. Пользователи жалуются, что не получают сообщения, если вводят уже существующую почту. Нам нужно настроить чёткие уведомления об ошибках в UI. Завтра Данила пришлет обновленные макеты хедера и главной страницы, чтобы мы могли приступить к финальной верстке личного кабинета."
  }
])

const view = (id) => console.log('Просмотр:', id)
const edit = (id) => console.log('Редактирование:', id)
const remove = (id) => {
  toast({
    component: ConfirmAction,
    listeners: {
      confirm: () => {
        performDelete(id); 
        toast.clear();
        toast.success("Удалено");
      }
    }
  }, {
    timeout: false,      
    closeOnClick: false,     
    draggable: false,        
    icon: false,             
    position: "top-center"   
  });
}
</script>
<style scoped>

</style>