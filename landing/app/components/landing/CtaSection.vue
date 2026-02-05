<script setup lang="ts">
import Button from '~/components/ui/Button.vue'
import DecryptedText from './DecryptedText.vue'
</script>

<template>
  <section class="py-16 md:py-24 bg-brand-primary text-white text-center">
    <div class="container mx-auto px-4 md:px-6">
      <h2 class="text-3xl md:text-5xl font-bold mb-6">
        <DecryptedText text="Ready to Supercharge Your Career?" animate-on="view" reveal-direction="center" />
      </h2>
      <p class="text-xl text-blue-100 max-w-2xl mx-auto mb-10">Join professionals who are landing their dream jobs faster with our AI tools.</p>
      <Button size="lg" to="/signup" class="bg-white text-brand-primary hover:bg-gray-100 focus:ring-white">
        Start Building for Free
      </Button>
      <p class="mt-6 text-sm text-blue-200">No credit card required • Cancel anytime</p>
    </div>
  </section>
</template>
