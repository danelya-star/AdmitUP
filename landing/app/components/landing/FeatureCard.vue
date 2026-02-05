<script setup lang="ts">
interface Props {
  title: string
  description: string
  icon?: string
}

defineProps<Props>()
</script>

<template>
  <div class="bg-gray-50 p-6 rounded-xl hover:bg-gray-100 transition-all duration-300 group">
    <div class="w-12 h-12 rounded-lg bg-blue-50 flex items-center justify-center mb-4 group-hover:bg-blue-100 transition-colors">
      <slot name="icon">
        <!-- Default icon if none provided -->
         <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-brand-secondary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
        </svg>
      </slot>
    </div>
    <h3 class="text-xl font-bold text-gray-900 mb-2">{{ title }}</h3>
    <p class="text-gray-600 leading-relaxed">{{ description }}</p>
  </div>
</template>
