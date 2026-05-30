<script setup>
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"
import { supabase } from "../supabase"
import { useToast } from "vue-toastification"

const toast = useToast()
const email = ref('')
const password = ref('')
const errorMessage = ref('')
const router = useRouter()

// БЛОКИРОВКА ДОСТУПА: Проверяем сессию при загрузке
onMounted(async () => {
  const { data: { session } } = await supabase.auth.getSession()
  if (session) {
    toast.info("Вы уже авторизованы!")
    router.push('/main') 
  }
})

const handleLogin = async () => {
    errorMessage.value = ''

    // Двойная проверка на случай быстрого клика
    const { data: { session } } = await supabase.auth.getSession()
    if (session) {
        toast.info("Вы уже авторизованы!")
        router.push('/main')
        return
    }

    const { data, error } = await supabase.auth.signInWithPassword({
        email: email.value,
        password: password.value
    })
    
    if (error) {
        errorMessage.value = error.message
        toast.error('Ошибка входа: ' + error.message)
    } else {
        toast.success('Вы успешно вошли в систему!')
        router.push('/') // Перекидываем на главную после входа
    }
}
</script>

<template>
    <div class="min-h-screen w-full flex items-center justify-center bg-slate-50 p-4 sm:p-8 font-sans">

        <div class="bg-white max-w-md w-full px-6 py-8 sm:px-10 sm:py-10 rounded-2xl border border-slate-100 shadow-xl text-center">

            <h2 class="text-2xl sm:text-3xl font-bold mb-8 sm:mb-10 text-slate-900 tracking-tight">
                Вход в аккаунт
            </h2>

            <form @submit.prevent="handleLogin" class="space-y-5 sm:space-y-6 text-left">

                <div>
                    <label for="email" class="block text-sm text-slate-500 mb-1.5 font-medium">Email</label>
                    <div class="relative group">
                        <svg xmlns="http://www.w3.org/2000/svg" class="absolute top-1/2 -translate-y-1/2 left-3.5 w-5 h-5 text-slate-400 group-hover:text-blue-500 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                        </svg>
                    
                        <input
                            v-model="email"
                            type="email"
                            id="email"
                            placeholder="example@gmail.com"
                            required
                            class="w-full pl-11 pr-4 py-3 border border-slate-200 rounded-lg placeholder:text-slate-300 focus:ring-2 focus:ring-blue-100 focus:border-blue-400 transition-all text-slate-900 outline-none"
                        />
                    </div>
                </div>

                <div>
                    <label for="password" class="block text-sm text-slate-500 mb-1.5 font-medium">Пароль</label>
                    <div class="relative group">
                        <svg xmlns="http://www.w3.org/2000/svg" class="absolute top-1/2 -translate-y-1/2 left-3.5 w-5 h-5 text-slate-400 group-hover:text-blue-500 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                        </svg>

                        <input 
                            v-model="password"
                            type="password"
                            id="password"
                            placeholder="•••••••"
                            required
                            class="w-full pl-11 pr-4 py-3 border border-slate-200 rounded-lg placeholder:text-slate-300 focus:ring-2 focus:ring-blue-100 focus:border-blue-400 transition-all text-slate-900 outline-none"
                        />
                    </div>
                </div>
                
                <button type="submit" class="w-full bg-[#0f172a] text-white py-3 sm:py-3.5 mt-2 rounded-lg font-semibold hover:bg-slate-800 transition-colors focus:ring-4 focus:ring-slate-300 outline-none">
                    Войти
                </button>
            </form>
            
            <div class="text-center mt-8 sm:mt-10 text-sm text-slate-500 space-y-3">
                <router-link to="/reset-password" class="block hover:text-blue-600 transition-colors">
                    Забыли пароль?
                </router-link>

                <div>
                    <span>Нет аккаунта?</span>
                    <router-link to="/register" class="font-medium text-slate-900 hover:text-blue-600 transition-colors ml-1.5">
                        Зарегистрируйтесь
                    </router-link>
                </div>
            </div>

        </div>
    </div>
</template>