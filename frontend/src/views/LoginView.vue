<template>
  <div style="max-width: 400px; margin: auto; padding: 1em;">
    <h2>Login</h2>
    <form @submit.prevent="doLogin">
      <div class="field">
        <label for="username">Username</label>
        <input id="username" v-model="username" required />
      </div>
      <div class="field">
        <label for="password">Password</label>
        <input id="password" type="password" v-model="password" required />
      </div>
      <button type="submit">Log In</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
    <p>
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
    async doLogin() {
      this.error = ''
      try {
        const res = await axios.post('/auth/login', {
          username: this.username,
          password: this.password
        })
        // Store the JWT and go to profiles page
        localStorage.setItem('jwt', res.data.access_token)
        this.$router.push('/profiles')
      } catch (e) {
        this.error = e.response?.data?.msg || 'Login failed'
      }
    }
  }
}
</script>

<style scoped>
.field { margin-bottom: 0.75em; }
.error { color: red; }
</style>
