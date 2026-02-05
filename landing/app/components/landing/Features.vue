<script setup lang="ts">
import FeatureCard from './FeatureCard.vue'

const features = [
  {
    title: 'AI Writing Checker',
    description: 'Get instant feedback on Task 1 and Task 2 essays with band score estimation and detailed corrections.',
    icon: 'file-text'
  },
  {
    title: 'Speaking Practice with AI',
    description: 'Practice IELTS Speaking parts 1–3 with an AI examiner and receive fluency, grammar, and pronunciation feedback.',
    icon: 'message-square'
  },
  {
    title: 'Smart Vocabulary Builder',
    description: 'Learn high-impact IELTS vocabulary with examples, synonyms, and real exam-style usage.',
    icon: 'globe'
  },
  {
    title: 'Personalized Study Plan',
    description: 'AI creates a custom IELTS study plan based on your current level, goals, and test date.',
    icon: 'layout'
  }
]
</script>

<template>
  <section id="features" class="py-16 md:py-24 bg-white">
    <div class="container mx-auto px-4 md:px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h2 class="text-3xl md:text-5xl font-bold text-brand-primary mb-4">Everything You Need to Ace IELTS</h2>
        <p class="text-lg text-gray-600">Powerful AI tools designed to help you achieve your target IELTS score.</p>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <FeatureCard 
          v-for="feature in features" 
          :key="feature.title"
          :title="feature.title" 
          :description="feature.description"
        >
          <template #icon>
            <!-- Hardcoded clear icons for now to avoid dependencies, can be replaced with lucide-vue-next later -->
            <svg v-if="feature.icon === 'file-text'" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-brand-secondary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            <svg v-else-if="feature.icon === 'layout'" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-brand-secondary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
            <svg v-else-if="feature.icon === 'globe'" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-brand-secondary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" /></svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-brand-secondary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" /></svg>
          </template>
        </FeatureCard>
      </div>
    </div>
  </section>
</template>
