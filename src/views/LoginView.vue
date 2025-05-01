<template>
  <div class="login-page">
    <h1>Login</h1>
    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label>Username</label>
        <input v-model="username" required />
      </div>
      <div class="form-group">
        <label>Password</label>
        <input v-model="password" type="password" required />
      </div>
      <button type="submit">Log In</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  setup() {
    const router = useRouter()
    return { router }
  },
  methods: {
    async onSubmit() {
      this.error = ''
      try {
        const res = await axios.post('/auth/login', {
          username: this.username,
          password: this.password
        })
        // save your token
        localStorage.setItem('jwt', res.data.access_token)
        // force a full reload so App.vue re-reads it
        window.location.href = '/'
      } catch (err) {
        this.error = err.response?.data?.msg || 'Login failed'
      }
    }
  }
}
</script>

<style scoped>
.login-page { max-width:400px; margin:2rem auto; }
.form-group { margin-bottom:1rem; }
.error { color: #e74c3c; }
</style>
