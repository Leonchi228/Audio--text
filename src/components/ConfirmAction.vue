<template>
  <div class="flex flex-col gap-3">
    <span class="text-sm font-medium">Вы уверены, что хотите удалить эту транскрибацию?</span>
    <div class="flex gap-2">
      <button 
        @click="$emit('confirm')" 
        class="bg-red-500 text-white px-3 py-1 rounded text-xs hover:bg-red-600"
      >
        Да, удалить
      </button>
      <button 
        @click="$emit('close-toast')" 
        class="bg-gray-200 text-gray-700 px-3 py-1 rounded text-xs hover:bg-gray-300"
      >
        Отмена
      </button>
    </div>
  </div>
</template>

<script setup>
defineEmits(['confirm', 'close-toast'])
</script>