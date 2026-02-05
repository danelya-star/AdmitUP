<script setup lang="ts">
import { ref, onMounted } from 'vue'
import Button from '~/components/ui/Button.vue'
import gsap from 'gsap'

const heroContentRef = ref<HTMLElement | null>(null)

onMounted(() => {
  if (heroContentRef.value) {
    const elements = heroContentRef.value.children
    gsap.fromTo(elements, 
      { opacity: 0 },
      { 
        opacity: 1, 
        duration: 0.8, 
        stagger: 0.2, 
        ease: 'power2.out',
        delay: 0.5 // Wait for header animation
      }
    )
  }
})
</script>

<template>
  <section class="relative overflow-hidden pt-16 pb-12 md:pt-24 md:pb-20 lg:pt-32 lg:pb-24">
    <div class="container mx-auto px-4 md:px-6">
      <div ref="heroContentRef" class="flex flex-col items-center text-center">
        <h1 class="text-4xl md:text-6xl font-bold tracking-tight text-brand-primary max-w-4xl mb-6">
          Build Your Dream Career with <span class="text-brand-secondary">AI-Powered</span> Tools
        </h1>
        <p class="text-xl text-gray-600 max-w-2xl mb-10 leading-relaxed">
          Create professional resumes, stunning portfolios, and get personalized career advice in seconds. Stand out from the crowd with the power of AI.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 w-full sm:w-auto">
          <Button size="lg" to="/signup">Get Started for Free</Button>
          <Button variant="outline" size="lg" to="#features">Learn More</Button>
        </div>
        
        <!-- Optional visual element/mockup could go here -->
        <div class="mt-16 relative z-10 w-full max-w-5xl mx-auto rounded-xl bg-white overflow-hidden border border-gray-100">
           <div class="aspect-[16/9] bg-gray-50 flex items-center justify-center">
              <span class="text-gray-400 font-medium">App Dashboard Mockup Placeholder</span>
           </div>
        </div>
      </div>
    </div>
    
    <!-- Decorative background elements -->
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full -z-10 pointer-events-none">
       <div class="absolute top-[20%] left-[10%] w-72 h-72 bg-blue-100 rounded-full blur-3xl opacity-60"></div>
       <div class="absolute bottom-[20%] right-[10%] w-96 h-96 bg-indigo-100 rounded-full blur-3xl opacity-60"></div>
    </div>
  </section>
</template>
