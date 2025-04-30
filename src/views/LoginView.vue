<template>
  <div class="auth-page">
    <h2>Log In</h2>
    <form @submit.prevent="onLogin">
      <div>
        <label for="username">Username</label><br>
        <input
          id="username"
          v-model="username"
          type="text"
          placeholder="Your username"
          required
        />
      </div>
      <div style="margin-top:0.5em;">
        <label for="password">Password</label><br>
        <input
          id="password"
          v-model="password"
          type="password"
          placeholder="Your password"
          required
        />
      </div>
      <button type="submit" style="margin-top:1em;">Log In</button>
    </form>

    <p v-if="error" class="error">{{ error }}</p>
    <p style="margin-top:1em;">
      Don’t have an account? 
      <router-link to="/register">Register here</router-link>.
    </p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  methods: {
    async onLogin() {
      this.error = ''
      try {
        const res = await axios.post('/auth/login', {
          username: this.username,
          password: this.password
        })
        // save JWT
        localStorage.setItem('jwt', res.data.access_token)
        // go to profiles list
        this.$router.push({ name: 'profiles' })
      } catch (e) {
        this.error = e.response?.data?.msg || 'Login failed'
      }
    }
  }
}
</script>

<style scoped>
.auth-page { max-width: 400px; margin: 2em auto; }
.error { color: red; margin-top: 1em; }
</style>
