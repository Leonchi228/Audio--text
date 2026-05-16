<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from "vue-toastification"
import { supabase } from '../supabase' 
import ConfirmAction from "../components/ConfirmAction.vue"

const router = useRouter()
const toast = useToast()

const transcriptions = ref([])
const isFetching = ref(false)

// cостояние для полного просмотра в модальном окне
const selectedItem = ref(null)

// Состояние для быстрого изменения названия
const editingId = ref(null)
const editTitle = ref('')

// 1. ПОЛУЧЕНИЕ ДАННЫХ ИЗ SUPABASE
const fetchTranscriptions = async () => {
  isFetching.value = true
  try {
    const { data: { session } } = await supabase.auth.getSession()
    if (!session) {
      toast.error("Пожалуйста, войдите в систему")
      router.push('/login') // Перенаправляем, если сессия сброшена
      return
    }

    // Загружаем записи конкретного юзера (сортируем от новых к старым)
    const { data, error } = await supabase
      .from('transcriptions')
      .select('*')
      .eq('user_id', session.user.id)
      .order('created_at', { ascending: false })

    if (error) throw error
    transcriptions.value = data
  } catch (error) {
    console.error('Ошибка загрузки данных:', error.message)
    toast.error('Не удалось загрузить историю транскрибаций')
  } finally {
    isFetching.value = false
  }
}

onMounted(() => {
  fetchTranscriptions()
})

// 2. РАЗВОРАЧИВАНИЕ (ПРОСМОТР)
const openViewModal = (item) => {
  selectedItem.value = item
}

// Копирование в буфер обмена прямо из модалки
const copyToClipboard = (text) => {
  navigator.clipboard.writeText(text)
  toast.success("Текст успешно скопирован!")
}

// 3. РЕДАКТИРОВАНИЕ (Включение инпута в карточке)
const startEdit = (item) => {
  editingId.value = item.id
  editTitle.value = item.title
}

const saveEdit = async (id) => {
  if (!editTitle.value.trim()) {
    toast.warning("Название файла не может быть пустым")
    return
  }

  try {
    const { error } = await supabase
      .from('transcriptions')
      .update({ title: editTitle.value })
      .eq('id', id)

    if (error) throw error

    // Обновляем состояние на фронтенде без перезагрузки всей страницы
    const item = transcriptions.value.find(t => t.id === id)
    if (item) item.title = editTitle.value
    
    editingId.value = null
    toast.success("Название успешно обновлено")
  } catch (error) {
    toast.error("Не удалось обновить название")
    console.error(error.message)
  }
}

// 4. ТВОЙ КОД УДАЛЕНИЯ С ПОДКЛЮЧЕНИЕМ SUPABASE БАЗЫ
const performDelete = async (id) => {
  try {
    const { error } = await supabase
      .from('transcriptions')
      .delete()
      .eq('id', id)

    if (error) throw error

    // Удаляем из локального массива Vue, чтобы карточка моментально исчезла
    transcriptions.value = transcriptions.value.filter(item => item.id !== id)
  } catch (error) {
    toast.error("Ошибка при удалении записи из БД")
    console.error(error.message)
  }
}

const remove = (id) => {
  toast({
    component: ConfirmAction,
    listeners: {
      confirm: () => {
        performDelete(id); 
        toast.clear();
        toast.success("Запись успешно удалена");
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

// Форматирование даты
const formatDate = (isoString) => {
  if (!isoString) return ''
  const date = new Date(isoString)
  return date.toLocaleString('ru-RU', {
    day: '2xl text-slate-900',
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

<template>
  <div class="min-h-screen bg-gray-50/50 pb-12 font-sans selection:bg-orange-100 selection:text-orange-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      
      <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-8">
        <div>
          <h1 class="text-2xl font-bold text-[#0B132B]">Мои транскрибации</h1>
          <p class="text-sm text-gray-500 mt-1">
            <span v-if="isFetching">Загрузка данных...</span>
            <span v-else>Всего обработано: {{ transcriptions.length }} файлов</span>
          </p>
        </div>
        <button 
          @click="router.push('/')"
          class="w-full sm:w-auto justify-center bg-[#0F172A] text-white px-5 py-2.5 rounded-lg text-sm font-medium hover:bg-slate-800 transition-all flex items-center gap-2"
        >
          <span>+</span> Новая транскрибация
        </button>
      </div>

      <div v-if="transcriptions.length === 0 && !isFetching" class="text-center py-16 bg-white rounded-xl border border-gray-200 shadow-sm p-6">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 text-gray-400 mx-auto mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 13h6m-3-3v6m-9 1V4a2 2 0 012-2h6l2 2h6a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2z" />
        </svg>
        <h3 class="text-base font-semibold text-gray-900 mb-1">У вас еще нет транскрибаций</h3>
        <p class="text-sm text-gray-500 mb-4">Загрузите свой первый аудио или видео файл прямо сейчас.</p>
        <button @click="router.push('/')" class="text-sm font-medium text-orange-500 hover:text-orange-600">Начать работу &rarr;</button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="item in transcriptions" 
          :key="item.id" 
          class="bg-white border border-gray-200 rounded-xl p-6 shadow-sm hover:shadow-md transition-shadow flex flex-col h-full"
        >
          <div class="mb-4">
            <div v-if="editingId === item.id" class="flex gap-2 items-center">
              <input 
                v-model="editTitle" 
                type="text" 
                class="w-full px-2 py-1 text-sm border rounded-md focus:outline-none focus:border-orange-500"
              />
              <button @click="saveEdit(item.id)" class="text-xs bg-green-500 text-white px-2 py-1 rounded hover:bg-green-600">✓</button>
              <button @click="editingId = null" class="text-xs bg-gray-300 text-gray-700 px-2 py-1 rounded hover:bg-gray-400">✕</button>
            </div>
            <h3 v-else class="font-semibold text-[#0B132B] truncate" :title="item.title">
              {{ item.title }}
            </h3>
            <span class="text-xs text-gray-400">{{ formatDate(item.created_at) }}</span>
          </div>

          <div class="flex-grow">
            <p class="text-sm text-gray-600 leading-relaxed line-clamp-5 mb-6 whitespace-pre-line">
              {{ item.content }}
            </p>
          </div>

          <div class="flex items-center justify-between pt-4 border-t border-gray-100 mt-auto gap-2">
            <div class="flex gap-2">
              <button 
                @click="openViewModal(item)"
                class="text-xs font-medium text-[#0F172A] hover:bg-slate-50 px-2.5 sm:px-3 py-1.5 rounded-md border border-gray-200 transition-colors"
              >
                Просмотреть
              </button>
              <button 
                @click="startEdit(item)"
                class="text-xs font-medium text-gray-600 hover:bg-slate-50 px-2.5 sm:px-3 py-1.5 rounded-md border border-gray-200 transition-colors"
              >
                Изменить
              </button>
            </div>
            
            <button 
              @click="remove(item.id)"
              class="text-xs font-medium text-red-500 hover:bg-red-50 px-2.5 sm:px-3 py-1.5 rounded-md transition-colors"
            >
              Удалить
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="selectedItem" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm animate-fade-in">
      <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[80vh] flex flex-col shadow-xl overflow-hidden">
        <div class="p-6 border-b border-gray-100 flex justify-between items-center bg-slate-50">
          <div class="min-w-0 pr-4">
            <h2 class="text-lg font-bold text-slate-900 truncate" :title="selectedItem.title">{{ selectedItem.title }}</h2>
            <p class="text-xs text-gray-400 mt-0.5">{{ formatDate(selectedItem.created_at) }}</p>
          </div>
          <button @click="selectedItem = null" class="p-1 rounded-lg hover:bg-gray-200 text-gray-500 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>
        <div class="p-6 overflow-y-auto flex-grow">
          <p class="text-sm sm:text-base text-gray-700 leading-relaxed whitespace-pre-line select-text">
            {{ selectedItem.content }}
          </p>
        </div>
        <div class="p-4 bg-gray-50 border-t border-gray-100 flex justify-end gap-3">
          <button 
            @click="copyToClipboard(selectedItem.content)"
            class="px-4 py-2 bg-orange-500 text-white text-sm font-medium rounded-lg hover:bg-orange-600 transition-colors"
          >
            Копировать текст
          </button>
          <button 
            @click="selectedItem = null"
            class="px-4 py-2 border border-gray-200 text-gray-700 text-sm font-medium rounded-lg hover:bg-gray-100 transition-colors"
          >
            Закрыть
          </button>
        </div>
      </div>
    </div>

  </div>
</template>


<style scoped>
.animate-fade-in {
  animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>