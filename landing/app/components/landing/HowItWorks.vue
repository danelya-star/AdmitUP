<script setup lang="ts">
import DecryptedText from './DecryptedText.vue'

const steps = [
  {
    id: 1,
    title: 'Sign Up',
    description: 'Create your free account in seconds. No credit card required.',
  },
  {
    id: 2,
    title: 'Input Your Data',
    description: 'Upload your LinkedIn PDF or manually enter your experience.',
  },
  {
    id: 3,
    title: 'Get Results',
    description: 'AI generates a polished resume and portfolio instantly.',
  },
]
</script>

<template>
  <section class="py-16 md:py-24 bg-gray-50">
    <div class="container mx-auto px-4 md:px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h2 class="text-3xl md:text-5xl font-bold text-brand-primary mb-4">
          <DecryptedText text="How It Works" animate-on="view" reveal-direction="center" />
        </h2>
        <p class="text-lg text-gray-600">Three simple steps to your new career.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
        <!-- Connecting line for desktop -->
        <div class="hidden md:block absolute top-12 left-[16%] right-[16%] h-0.5 bg-gray-200 -z-10"></div>

        <div v-for="step in steps" :key="step.id" class="flex flex-col items-center text-center relative">
          <div class="w-24 h-24 bg-white rounded-full flex items-center justify-center border border-gray-100 mb-6 z-10">
            <span class="text-3xl font-bold text-brand-secondary">{{ step.id }}</span>
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">{{ step.title }}</h3>
          <p class="text-gray-600 max-w-xs">{{ step.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
