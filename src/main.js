// src/main.js
import { createApp } from 'vue'
import App          from './App.vue'
import router       from './router'           // ← your index.js
import axios        from 'axios'

// point axios at your Flask API
axios.defaults.baseURL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5001/api'
axios.interceptors.request.use(cfg => {
  const jwt = localStorage.getItem('jwt')
  if (jwt) cfg.headers.Authorization = `Bearer ${jwt}`
  return cfg
})

createApp(App)
  .use(router)              // ← install the router
  .mount('#app')
