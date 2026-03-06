<template>
  <nav class="bg-white border-b border-gray-200 w-full fixed shadow">
    <div class="max-w-7xl mx-auto px-6 py-4 bg-white flex justify-between items-center">
      <div class="flex items-center gap-2 font-semibold text-lg">
        🔵 Calculadora de IRS
      </div>

      <div class="flex flex-col gap-6 text-sm p-3
      text-gray-600 bg-white fixed top-15 h-50 left-0 w-full shadow-lg
      md:relative md:h-auto md:top-auto md:left-auto md:flex-row md:w-auto md:shadow-none transition-all duration-500
      md:items-center" :class="{'opacity-0': !isOpen, 'opacity-100': isOpen}" >
        <a href="#">Simulador</a>
        <a href="#">Guia Fiscal</a>
        <a href="#">Contactos</a>
        <button class="bg-blue-600 text-white px-4 py-2 rounded-lg">
          Entrar
        </button>
      </div>

      <div v-if="isMobile">
        <button @click="isOpen = true" v-if="!isOpen">
          <span class="material-symbols-outlined">
              menu
                </span>
        </button>
      <button @click="isOpen = false" v-else>
        <span class="material-symbols-outlined">
              close
        </span>
      </button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue';


const isMobile = ref(window.innerWidth < 768)
const isOpen = ref(window.innerWidth >= 768)

const toggleMenu = function(){
    isMobile.value = window.innerWidth < 768
    isOpen.value = isMobile.value ? false : true
}

onMounted(()=>{
  window.addEventListener("resize", toggleMenu)
})


</script>