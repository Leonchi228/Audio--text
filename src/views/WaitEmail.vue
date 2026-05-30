<script setup>
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"
import { supabase } from "../supabase"
import { useToast } from "vue-toastification"

const router = useRouter()
const email = ref('')
const toast = useToast()

onMounted(() => {
    supabase.auth.onAuthStateChange((event, session) => {
        if (event === 'PASSWORD_RECOVERY') {
            router.push('/update-password')
        }
    })
})

const handleReset = async () => {
    if (!email.value) {
        toast.error("Пожалуйста, введите ваш Email")
        return
    }

    const { data, error } = await supabase.auth.resetPasswordForEmail(email.value, {
        redirectTo: `${window.location.origin}/update-password`,
    })

    if (error) {
        toast.error('Ошибка: ' + error.message)
    } else {
        toast.success('Письмо для восстановления отправлено на вашу почту!')
        email.value = '' 
    }
}
</script>

<template>
    <div class="min-h-screen w-full flex items-center justify-center bg-slate-50 p-4 sm:p-8 font-sans">

        <div class="bg-white max-w-md w-full px-6 py-8 sm:px-10 sm:py-10 rounded-2xl border border-slate-100 shadow-xl text-center">

            <h2 class="text-2xl sm:text-3xl font-bold mb-8 sm:mb-10 text-slate-900 tracking-tight">
                Восстановление пароля
            </h2>

            <form @submit.prevent="handleReset" class="space-y-5 sm:space-y-6 text-left">

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

                <button type="submit" class="w-full bg-[#0f172a] text-white py-3 sm:py-3.5 mt-2 rounded-lg font-semibold hover:bg-slate-800 transition-colors focus:ring-4 focus:ring-slate-300 outline-none">
                    Восстановить
                </button>
            </form>
        
            <div class="text-center mt-8 sm:mt-10 text-sm text-slate-500">
                <span>Вспомнили пароль?</span>
                <router-link to="/login" class="font-medium text-slate-900 hover:text-blue-600 transition-colors ml-1.5">
                    Войти в аккаунт
                </router-link>
            </div>    
            
        </div>
    </div>
</template>