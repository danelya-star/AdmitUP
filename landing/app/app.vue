<template>
  <NuxtLayout>
    <AppHeader />
    <Analytics/>
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { Analytics } from '@vercel/analytics/nuxt'
import AppHeader from '~/components/landing/AppHeader.vue'
</script> 