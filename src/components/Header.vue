<template>
  <header class="w-full bg-white border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-14">
        
        <div class="shrink-0 flex items-center">
          <router-link to="/" class="text-[22px] font-semibold text-[#0B132B] tracking-tight">
            Транскрибатор
          </router-link>
        </div>

        <nav class="hidden md:flex items-center space-x-8">
          <router-link to="/" class="text-[15px] font-medium text-gray-500 hover:text-[#0B132B] transition-colors">
  Главная
</router-link>
          
          <router-link to="/api" class="text-[15px] font-medium text-gray-500 hover:text-[#0B132B] transition-colors">
            API
          </router-link>
          
          <router-link to="/docs" class="text-[15px] font-medium text-gray-500 hover:text-[#0B132B] transition-colors">
            Документация
          </router-link>
          
          <router-link to="/support" class="text-[15px] font-medium text-gray-500 hover:text-[#0B132B] transition-colors">
            Поддержка
          </router-link>

          <div class="flex items-center space-x-4 ml-4">
            <template v-if="isLoggedIn">
              <router-link 
                to="/private" 
                class="text-[15px] font-medium text-gray-500 hover:text-[#0B132B] transition-colors"
              >
                Личный кабинет
              </router-link>

              <button 
                @click="handleLogout"
                class="px-4 py-2 border border-gray-200 text-[#0B132B] text-[13px] font-medium rounded-lg hover:bg-gray-50 transition-all"
              >
                Выйти
              </button>
            </template>

            <template v-else>
              <router-link 
                to="/login" 
                class="px-6 py-2 bg-[#0F172A] text-white text-[15px] font-medium rounded-lg hover:bg-slate-800 transition-all shadow-sm"
              >
                Войти
              </router-link>
            </template>
          </div>
        </nav>

      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, computed } from "vue"
import { supabase } from "../supabase.js"
import { useRouter } from "vue-router"

const user = ref(null)
const router = useRouter()


const isLoggedIn = computed(() => user.value !== null)

const handleLogout = async () => {
  await supabase.auth.signOut()
  user.value = null 
  router.push('/')
}

onMounted(async () => {

  const { data: { session } } = await supabase.auth.getSession()
  user.value = session?.user || null

  supabase.auth.onAuthStateChange((event, session) => {
    user.value = session?.user || null
  })
})
</script>


<style scoped>

</style>