<!-- frontend/src/components/ThemeToggle.vue -->
<template>
  <button @click="toggleTheme" class="theme-toggle">
    {{ theme === 'light' ? '🌙 Dark' : '☀️ Light' }}
  </button>
</template>

<script>
export default {
  name: 'ThemeToggle',
  data() {
    return {
      theme: localStorage.getItem('theme') || 'light'
    }
  },
  mounted() {
    document.documentElement.setAttribute('data-theme', this.theme)
  },
  methods: {
    toggleTheme() {
      this.theme = this.theme === 'light' ? 'dark' : 'light'
      document.documentElement.setAttribute('data-theme', this.theme)
      localStorage.setItem('theme', this.theme)
    }
  }
}
</script>

<style>
.theme-toggle {
  background: none;
  border: 1px solid currentColor;
  padding: 0.3em 0.6em;
  border-radius: 4px;
  cursor: pointer;
}
</style>
