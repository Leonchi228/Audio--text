<script setup>
import { ref } from "vue"
import { supabase } from "../supabase"
import { useToast } from "vue-toastification"

const email = ref('')
const isEmailSent = ref(false)
const loading = ref(false)
const toast = useToast()

const handleResetPassword = async () => {
    if (!email.value) {
        toast.error("Пожалуйста, введите ваш Email")
        return
    }

    loading.value = true

    const { error } = await supabase.auth.resetPasswordForEmail(email.value, {
        redirectTo: `${window.location.origin}/update-password`
    })
    
    if (error) {
        toast.error('Ошибка: ' + error.message)
    } else {
        isEmailSent.value = true

    }
    
    loading.value = false
}
</script>

<template>
    <div class="min-h-screen w-full flex flex-col justify-center bg-white sm:bg-slate-50 font-sans">

        <div v-if="!isEmailSent" class="w-full max-w-md mx-auto px-6 py-10 sm:px-10 sm:py-10 sm:bg-white sm:rounded-2xl sm:border sm:border-slate-100 sm:shadow-xl text-center">

            <h2 class="text-3xl font-bold mb-8 sm:mb-10 text-slate-900 tracking-tight">
                Восстановление
            </h2>

            <form @submit.prevent="handleResetPassword" class="space-y-6 text-left">
                <div>
                    <label for="email" class="block text-sm text-slate-500 mb-2 font-medium">Email</label>
                    <div class="relative group">
                        <svg xmlns="http://www.w3.org/2000/svg" class="absolute top-1/2 -translate-y-1/2 left-4 w-5 h-5 text-slate-400 group-hover:text-blue-500 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                        </svg>
                        <input
                            v-model="email"
                            type="email"
                            id="email"
                            placeholder="example@gmail.com"
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
                    {{ loading ? 'Отправка...' : 'Восстановить' }}
                </button>
            </form>
        
            <div class="text-center mt-10 text-base sm:text-sm text-slate-500">
                <router-link to="/login" class="font-semibold text-slate-900 hover:text-blue-600 transition-colors">
                    Вернуться ко входу
                </router-link>
            </div>    
        </div>

        <div v-else class="w-full max-w-md mx-auto px-6 py-10 sm:px-10 sm:py-12 sm:bg-white sm:rounded-2xl sm:border sm:border-slate-100 sm:shadow-xl text-center">
            
            <div class="mx-auto w-16 h-16 bg-green-50 rounded-full flex items-center justify-center mb-6">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                </svg>
            </div>

            <h2 class="text-2xl sm:text-3xl font-bold mb-4 text-slate-900 tracking-tight">
                Письмо отправлено
            </h2>
            
            <p class="text-slate-500 mb-8 text-base sm:text-sm leading-relaxed">
                Мы отправили инструкции по восстановлению пароля на <span class="font-medium text-slate-900">{{ email }}</span>. Пожалуйста, проверьте папку «Входящие» и «Спам».
            </p>
            
            <router-link to="/login" class="inline-flex justify-center w-full bg-slate-900 text-white py-4 sm:py-3.5 rounded-xl sm:rounded-lg font-semibold hover:bg-slate-800 transition-colors outline-none text-base">
                Вернуться ко входу
            </router-link>
        </div>

    </div>
</template>