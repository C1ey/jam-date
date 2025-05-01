// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

// ← point axios at your Flask API
axios.defaults.baseURL               = import.meta.env.VITE_API_URL
axios.defaults.headers.common[
  import.meta.env.VITE_JWT_HEADER
] = ''  // we’ll set this on each request via interceptor

// automatically attach JWT from localStorage
axios.interceptors.request.use(cfg => {
  const token = localStorage.getItem('jwt')
  if (token) {
    cfg.headers[ import.meta.env.VITE_JWT_HEADER ] = `Bearer ${token}`
  }
  return cfg
})

const app = createApp(App)
app.use(router)
app.mount('#app')

// for debugging
window.axios = axios
console.log('API baseURL:', axios.defaults.baseURL)
