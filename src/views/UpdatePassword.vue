<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import { supabase } from "../supabase"
import { useToast } from "vue-toastification"

const router = useRouter()
const toast = useToast()

const newPassword = ref('')
const loading = ref(false)

const handleUpdatePassword = async () => {
    // Проверка, что поле не пустое
    if (!newPassword.value) {
        toast.error("Введите новый пароль")
        return
    }

    loading.value = true
    
    // Запрос к Supabase на обновление пароля текущего пользователя
    const { error } = await supabase.auth.updateUser({
        password: newPassword.value
    })
    
    if (error) {
        toast.error('Ошибка: ' + error.message)
    } else {
        toast.success('Пароль успешно обновлен!')
        router.push('/login')
    }
    
    loading.value = false
}
</script>

<template>
    <div class="min-h-screen w-full flex flex-col justify-center bg-white sm:bg-slate-50 font-sans">
        
        <div class="w-full max-w-md mx-auto px-6 py-10 sm:px-10 sm:py-10 sm:bg-white sm:rounded-2xl sm:border sm:border-slate-100 sm:shadow-xl text-center">

            <h2 class="text-3xl font-bold mb-8 sm:mb-10 text-slate-900 tracking-tight">
                Новый пароль
            </h2>

            <form @submit.prevent="handleUpdatePassword" class="space-y-6 text-left">
                <div>
                    <label for="newPassword" class="block text-sm text-slate-500 mb-2 font-medium">Введите новый пароль</label>
                    <div class="relative group">
                        <svg xmlns="http://www.w3.org/2000/svg" class="absolute top-1/2 -translate-y-1/2 left-4 w-5 h-5 text-slate-400 group-hover:text-blue-500 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                        </svg>
                        <input
                            v-model="newPassword"
                            type="password"
                            id="newPassword"
                            placeholder="•••••••"
                            required
                            class="w-full pl-12 pr-4 py-3.5 sm:py-3 border border-slate-200 rounded-xl sm:rounded-lg placeholder:text-slate-300 focus:ring-2 focus:ring-blue-100 focus:border-blue-400 transition-all text-base sm:text-sm text-slate-900 outline-none"
                        />
                    </div>
                </div>

                <button 
                    type="submit" 
                    :disabled="loading"
                    class="w-full bg-slate-900 text-white py-4 sm:py-3.5 mt-4 rounded-xl sm:rounded-lg font-semibold hover:bg-slate-800 transition-colors focus:ring-4 focus:ring-slate-300 outline-none text-base disabled:opacity-70 disabled:cursor-not-allowed"
                >
                    {{ loading ? 'Сохранение...' : 'Установить пароль' }}
                </button>
            </form>
        
            <div class="text-center mt-10 text-base sm:text-sm text-slate-500">
                <router-link to="/login" class="font-semibold text-slate-900 hover:text-blue-600 transition-colors">
                    Вернуться ко входу
                </router-link>
            </div>    
            
        </div>
    </div>
</template>