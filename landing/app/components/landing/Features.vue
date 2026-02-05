<script setup lang="ts">
import FeatureCard from './FeatureCard.vue'
import DecryptedText from './DecryptedText.vue'

const features = [
  {
    title: 'AI Resume Builder',
    description: 'Generate ATS-friendly resumes tailored to specific job descriptions in seconds.',
    icon: 'file-text'
  },
  {
    title: 'Instant Portfolio',
    description: 'Create stunning portfolio websites from your GitHub or LinkedIn profile automatically.',
    icon: 'layout'
  },
  {
    title: 'Custom Domains',
    description: 'Connect your own domain name to build your personal brand professionally.',
    icon: 'globe'
  },
  {
    title: 'Career Copilot',
    description: 'Get real-time feedback on your application materials and interview tips.',
    icon: 'message-square'
  }
]
</script>

<template>
  <section id="features" class="py-16 md:py-24 bg-white">
    <div class="container mx-auto px-4 md:px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h2 class="text-3xl md:text-5xl font-bold text-brand-primary mb-4">
          <DecryptedText text="Everything You Need to Succeed" animate-on="view" reveal-direction="center" />
        </h2>
        <p class="text-lg text-gray-600">Powerful AI tools designed to help you land your dream job faster.</p>
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
            <svg v-else-if="feature.icon === 'layout'" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-brand-secondary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z" /></svg>
            <svg v-else-if="feature.icon === 'globe'" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-brand-secondary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" /></svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-brand-secondary" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" /></svg>
          </template>
        </FeatureCard>
      </div>
    </div>
  </section>
</template>
