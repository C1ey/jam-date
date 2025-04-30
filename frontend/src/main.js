import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

// Expose axios to the window for debugging
window.axios = axios

// Debug print your configured API URL
console.log('VITE_API_URL =', import.meta.env.VITE_API_URL)

// Correctly assign the base URL for all axios requests
axios.defaults.baseURL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5001/api'

// Automatically attach JWT from localStorage on every request
axios.interceptors.request.use(config => {
  const token = localStorage.getItem('jwt')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
}, err => Promise.reject(err))

createApp(App)
  .use(router)
  .mount('#app')
