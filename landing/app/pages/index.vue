<script setup lang="ts">
import Hero from '~/components/landing/Hero.vue'
import Features from '~/components/landing/Features.vue'
import HowItWorks from '~/components/landing/HowItWorks.vue'
import Testimonials from '~/components/landing/Testimonials.vue'
import CtaSection from '~/components/landing/CtaSection.vue'
import AppFooter from '~/components/AppFooter.vue'

useHead({
  title: 'AI Career Builder - Resume & Portfolio Generator',
  meta: [
    { name: 'description', content: 'Create professional resumes and portfolios in seconds with our AI-powered career tools.' }
  ],
  htmlAttrs: {
    lang: 'en'
  }
})
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <!-- Simple Navbar -->
    <header class="fixed top-0 w-full z-50 bg-white/80 backdrop-blur-md border-b border-gray-100">
      <div class="container mx-auto px-4 md:px-6 h-16 flex items-center justify-between">
        <a href="#" class="text-xl font-bold text-brand-primary flex items-center gap-2">
          <div class="w-8 h-8 bg-brand-secondary rounded-lg"></div>
          AI Career
        </a>
        <nav class="hidden md:flex gap-8">
          <a href="#features" class="text-sm font-medium text-gray-600 hover:text-brand-secondary transition-colors">Features</a>
          <a href="#" class="text-sm font-medium text-gray-600 hover:text-brand-secondary transition-colors">How it Works</a>
          <a href="#" class="text-sm font-medium text-gray-600 hover:text-brand-secondary transition-colors">Pricing</a>
        </nav>
        <div class="flex items-center gap-4">
          <a href="#" class="text-sm font-medium text-gray-600 hover:text-brand-primary hidden sm:block">Log in</a>
          <NuxtLink to="/signup" class="bg-brand-secondary text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-blue-600 transition-colors">
            Get Started
          </NuxtLink>
        </div>
      </div>
    </header>

    <main class="flex-grow">
      <Hero />
      <Features />
      <HowItWorks />
      <Testimonials />
      <CtaSection />
    </main>

    <AppFooter />
  </div>
</template>
