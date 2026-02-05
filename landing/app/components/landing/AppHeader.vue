<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import Button from '~/components/ui/Button.vue'
import gsap from 'gsap'

const isMobileMenuOpen = ref(false)
const mobileMenuRef = ref<HTMLElement | null>(null)
const headerRef = ref<HTMLElement | null>(null)
const logoRef = ref<HTMLElement | null>(null)
const navLinksRef = ref<HTMLElement[]>([])
const authButtonsRef = ref<HTMLElement | null>(null)

// Function to collect nav refs
const addNavLinkRef = (el: any) => {
  if (el) navLinksRef.value.push(el)
}

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
  
  if (isMobileMenuOpen.value) {
    document.body.style.overflow = 'hidden'
    // Animate menu opening
    gsap.to(mobileMenuRef.value, {
      height: '100vh',
      opacity: 1,
      duration: 0.5,
      ease: 'power3.out',
      display: 'block'
    })
    
    // Stagger items in mobile menu
    gsap.fromTo('.mobile-nav-item', 
      { opacity: 0 },
      { opacity: 1, duration: 0.4, stagger: 0.1, delay: 0.2, ease: 'power2.out' }
    )
  } else {
    document.body.style.overflow = ''
    // Animate menu closing
    gsap.to(mobileMenuRef.value, {
      opacity: 0,
      duration: 0.3,
      ease: 'power3.in',
      onComplete: () => {
        if (mobileMenuRef.value) {
            mobileMenuRef.value.style.display = 'none'
            // Reset height for next open
            gsap.set(mobileMenuRef.value, { height: 0 })
        }
      }
    })
  }
}

onMounted(() => {
  // Staggered fade in for header elements on load
  const tl = gsap.timeline()
  
  tl.from(logoRef.value, {
    opacity: 0,
    duration: 0.6,
    ease: 'power2.out'
  })
  .from(navLinksRef.value, {
    opacity: 0,
    duration: 0.6,
    stagger: 0.1,
    ease: 'power2.out'
  }, '-=0.4')
  .from(authButtonsRef.value, {
    opacity: 0,
    duration: 0.6,
    ease: 'power2.out'
  }, '-=0.4')
})
</script>

<template>
  <header ref="headerRef" class="fixed top-0 left-0 w-full bg-white/80 backdrop-blur-md border-b border-gray-100 z-50">
    <div class="container mx-auto px-4 md:px-6">
      <div class="flex items-center justify-between h-16 md:h-20">
        <!-- Logo -->
        <div ref="logoRef" class="flex items-center gap-2">
          <div class="w-8 h-8 bg-brand-secondary rounded-lg"></div>
          <span class="text-xl font-bold text-brand-primary">AI Career</span>
        </div>

        <!-- Desktop Navigation -->
        <nav class="hidden md:flex items-center space-x-8">
          <NuxtLink to="#features" class="text-gray-600 hover:text-brand-secondary transition-colors" :ref="addNavLinkRef">Features</NuxtLink>
          <NuxtLink to="#how-it-works" class="text-gray-600 hover:text-brand-secondary transition-colors" :ref="addNavLinkRef">How It Works</NuxtLink>
          <NuxtLink to="#pricing" class="text-gray-600 hover:text-brand-secondary transition-colors" :ref="addNavLinkRef">Pricing</NuxtLink>
        </nav>

        <!-- Auth Buttons -->
        <div ref="authButtonsRef" class="hidden md:flex items-center gap-4">
          <NuxtLink to="/login" class="text-gray-600 hover:text-brand-secondary font-medium transition-colors">Log In</NuxtLink>
          <Button to="/signup">Get Started</Button>
        </div>

        <!-- Mobile Menu Button -->
        <button @click="toggleMobileMenu" class="md:hidden p-2 text-gray-600 hover:text-brand-primary z-50 relative">
          <span class="sr-only">Toggle menu</span>
          <div class="w-6 h-5 flex flex-col justify-between">
            <span class="w-full h-0.5 bg-current transform transition-all duration-300" :class="{ 'rotate-45 translate-y-2': isMobileMenuOpen }"></span>
            <span class="w-full h-0.5 bg-current transition-all duration-300" :class="{ 'opacity-0': isMobileMenuOpen }"></span>
            <span class="w-full h-0.5 bg-current transform transition-all duration-300" :class="{ '-rotate-45 -translate-y-2.5': isMobileMenuOpen }"></span>
          </div>
        </button>
      </div>
    </div>

    <!-- Mobile Menu Overlay -->
    <div ref="mobileMenuRef" class="fixed inset-0 bg-white/95 backdrop-blur-sm z-40 hidden md:hidden pt-24 px-6 overflow-y-auto">
      <nav class="flex flex-col space-y-6 text-center">
        <NuxtLink to="#features" @click="toggleMobileMenu" class="mobile-nav-item text-xl font-medium text-gray-800">Features</NuxtLink>
        <NuxtLink to="#how-it-works" @click="toggleMobileMenu" class="mobile-nav-item text-xl font-medium text-gray-800">How It Works</NuxtLink>
        <NuxtLink to="#pricing" @click="toggleMobileMenu" class="mobile-nav-item text-xl font-medium text-gray-800">Pricing</NuxtLink>
        <hr class="border-gray-100 mobile-nav-item" />
        <NuxtLink to="/login" @click="toggleMobileMenu" class="mobile-nav-item text-xl font-medium text-gray-600">Log In</NuxtLink>
        <div class="mobile-nav-item pt-4">
          <Button to="/signup" class="w-full justify-center">Get Started</Button>
        </div>
      </nav>
    </div>
  </header>
</template>
