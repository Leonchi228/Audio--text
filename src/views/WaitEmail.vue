<script setup>
import { ref } from "vue"
import {useRouter} from "vue-router"
import axios from "axios"
import { supabase } from "../supabase"
import { onMounted } from "vue"

const router = useRouter()
const email = ref('')



onMounted(() => {
    supabase.auth.onAuthStateChange((event, session) => {
        if (event === 'PASSWORD_RECOVERY') {
            router.push('/update-password')
        }
    })})
</script>

<template>
    <div class="w-screen h-screen flex items-center justify-center bg-slate-50 px-15 py-42 font-sans">

    <div class="bg-white max-w-md w-full px-10 py-10 rounded-2xl border border-slate-100 shadow-xl text-center h-11/10">

        <h2 class="text-3xl font-bold mb-5 text-slate-900 tracking-tight">
            Восстановление пароля
        </h2>

        <form @submit.prevent = "handleLogin" class ="space-y-6 text-left">

            <div>
                <label for="email" class = "block text-sm text-slate-500 mb-1.5 font-medium">Email</label>

                <div class = "relative-group">
                    <svg xmlns = "http://www.w3.org/2000/svg" class="absolute top-1/2 -translate-y-1/2 left-3/5 w-5 h-5 text-slate-400 group-hover:text-blue-500 transition-colors" fill="none" viewBox="0 0 24 0" stroke="currentColor">
                        <path stroke-linecap ="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                    </svg>
                
                <input
                v-model="email"
                type="email"
                id="email"
                placeholder="example@gmail.com"
                class = "w-full pl-11 pr-4 py-3 border border-slate-200 rounded-lg placeholder:text-slate-300 focus:ring-2 focus:ring-blue-100 focus:border-blue-400 transition-all text-slate-900"
                />
                </div>
            </div>


            <button type="submit" class="w-full bg-[#0f172a] text-white py-3.5 rounded-lg font-semibold hover:bg-slate-800 transition-colors focus:ring-4 focus:ring-slate-300">
                Восстановить
            </button>
        </form>
        
        <div class="text-center mt-5 text-sm text-slate-500 space-y-3 "></div>
        <div>
            <router-link to="/login" class="font-medium text-slate-900 hover:text-blue-600 transition-colors ml-1.5">
                Войти в аккаунт
            </router-link>
        </div>    
        </div>
        </div>
</template>
    