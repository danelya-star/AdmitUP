<script setup lang="ts">
const testimonials = [
  {
    quote: "I landed my dream job at a top tech company thanks to the resume I built here. The AI suggestions were spot on!",
    author: "Sarah J.",
    role: "Product Designer"
  },
  {
    quote: "The portfolio builder is a game changer. I had a professional site up in minutes without writing a single line of code.",
    author: "Michael T.",
    role: "Software Engineer"
  },
  {
    quote: "Incredible tool. It helped me rephrase my experience to highlight my achievements much better than I could alone.",
    author: "Elena R.",
    role: "Marketing Manager"
  }
]
</script>

<template>
  <section class="py-16 md:py-24 bg-white border-t border-gray-100">
    <div class="container mx-auto px-4 md:px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h2 class="text-3xl md:text-5xl font-bold text-brand-primary mb-4">Trusted by Professionals</h2>
        <p class="text-lg text-gray-600">Join thousands of users who have advanced their careers.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div v-for="(testimonial, index) in testimonials" :key="index" class="bg-gray-50 p-8 rounded-2xl">
          <div class="flex text-brand-secondary mb-4">
            <svg v-for="i in 5" :key="i" class="w-5 h-5 fill-current" viewBox="0 0 20 20">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
            </svg>
          </div>
          <p class="text-gray-700 italic mb-6">"{{ testimonial.quote }}"</p>
          <div class="font-medium">
            <div class="text-gray-900">{{ testimonial.author }}</div>
            <div class="text-sm text-gray-500">{{ testimonial.role }}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
