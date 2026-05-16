<template>
  <header class="w-full bg-white border-b border-gray-100 sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-14">
        
        <div class="shrink-0 flex items-center">
          <router-link to="/" class="text-[22px] font-semibold text-[#0B132B] tracking-tight">
            Транскрибатор
          </router-link>
        </div>

        <nav class="hidden md:flex items-center space-x-8">
          <router-link to="/" class="text-[15px] font-medium text-gray-500 hover:text-[#0B132B] transition-colors" active-class="text-[#0B132B]">
            Главная
          </router-link>
          
          <router-link to="/api" class="text-[15px] font-medium text-gray-500 hover:text-[#0B132B] transition-colors" active-class="text-[#0B132B]">
            API
          </router-link>
          
          <router-link to="/doc" class="text-[15px] font-medium text-gray-500 hover:text-[#0B132B] transition-colors" active-class="text-[#0B132B]">
            Документация
          </router-link>
          
          <div class="flex items-center space-x-4 ml-4">
            <template v-if="isLoggedIn">
              <router-link 
                to="/private" 
                class="text-[15px] font-medium text-gray-500 hover:text-[#0B132B] transition-colors"
                active-class="text-[#0B132B]"
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

        <div class="flex md:hidden">
          <button 
            @click="isMenuOpen = !isMenuOpen" 
            type="button" 
            class="text-gray-500 hover:text-[#0B132B] focus:outline-none p-2 rounded-md"
          >
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path 
                v-if="!isMenuOpen" 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2" 
                d="M4 6h16M4 12h16M4 18h16" 
              />
              <path 
                v-else 
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2" 
                d="M6 18L18 6M6 6l12 12" 
              />
            </svg>
          </button>
        </div>

      </div>
    </div>

    <div v-if="isMenuOpen" class="md:hidden border-t border-gray-100 bg-white">
      <div class="px-4 pt-2 pb-4 space-y-3 shadow-inner">
        <router-link 
          to="/" 
          @click="isMenuOpen = false"
          class="block text-[15px] font-medium text-gray-600 hover:text-[#0B132B] py-2"
          active-class="text-[#0B132B] font-semibold"
        >
          Главная
        </router-link>
        
        <router-link 
          to="/api" 
          @click="isMenuOpen = false"
          class="block text-[15px] font-medium text-gray-600 hover:text-[#0B132B] py-2"
          active-class="text-[#0B132B] font-semibold"
        >
          API
        </router-link>
        
        <router-link 
          to="/doc" 
          @click="isMenuOpen = false"
          class="block text-[15px] font-medium text-gray-600 hover:text-[#0B132B] py-2"
          active-class="text-[#0B132B] font-semibold"
        >
          Документация
        </router-link>

        <hr class="border-gray-100 my-2" />

        <template v-if="isLoggedIn">
          <router-link 
            to="/private" 
            @click="isMenuOpen = false"
            class="block text-[15px] font-medium text-gray-600 hover:text-[#0B132B] py-2"
            active-class="text-[#0B132B] font-semibold"
          >
            Личный кабинет
          </router-link>

          <button 
            @click="handleMobileLogout"
            class="w-full mt-2 text-center px-4 py-2 border border-gray-200 text-red-600 text-[14px] font-medium rounded-lg hover:bg-gray-50 transition-all"
          >
            Выйти из аккаунта
          </button>
        </template>

        <template v-else>
          <router-link 
            to="/login" 
            @click="isMenuOpen = false"
            class="block w-full text-center px-6 py-2.5 bg-[#0F172A] text-white text-[15px] font-medium rounded-lg hover:bg-slate-800 transition-all shadow-sm"
          >
            Войти
          </router-link>
        </template>
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

const isMenuOpen = ref(false)

const isLoggedIn = computed(() => user.value !== null)

const handleLogout = async () => {
  await supabase.auth.signOut()
  user.value = null 
  router.push('/')
}


const handleMobileLogout = async () => {
  isMenuOpen.value = false
  await handleLogout()
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
/* Дополнительные стили больше не требуются, всё сделано на чистом Tailwind */
</style>