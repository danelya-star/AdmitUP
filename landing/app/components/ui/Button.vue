<script setup lang="ts">
interface Props {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost'
  size?: 'sm' | 'md' | 'lg'
  block?: boolean
  to?: string
  href?: string
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md',
  block: false,
})

const baseStyles = 'inline-flex items-center justify-center rounded-lg font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-brand-secondary focus:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none cursor-pointer'

const variantStyles = {
  primary: 'bg-brand-secondary text-white hover:bg-blue-600',
  secondary: 'bg-brand-primary text-white hover:bg-slate-800',
  outline: 'border border-gray-300 bg-transparent hover:bg-gray-100 text-gray-700',
  ghost: 'bg-transparent hover:bg-gray-100 text-gray-700',
}

const sizeStyles = {
  sm: 'h-9 px-3 text-sm',
  md: 'h-11 px-6 text-base',
  lg: 'h-14 px-8 text-lg',
}

const componentType = computed(() => {
  if (props.to) return resolveComponent('NuxtLink')
  if (props.href) return 'a'
  return 'button'
})
</script>

<template>
  <component
    :is="componentType"
    :to="to"
    :href="href"
    :class="[
      baseStyles,
      variantStyles[variant],
      sizeStyles[size],
      block ? 'w-full' : '',
    ]"
  >
    <slot />
  </component>
</template>
