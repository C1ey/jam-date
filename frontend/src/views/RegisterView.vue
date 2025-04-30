<template>
  <div style="max-width: 400px; margin: auto; padding: 1em;">
    <h2>Register</h2>
    <form @submit.prevent="doRegister">
      <div class="field">
        <label for="username">Username</label>
        <input id="username" v-model="username" required />
      </div>
      <div class="field">
        <label for="password">Password</label>
        <input id="password" type="password" v-model="password" required />
      </div>
      <button type="submit">Sign Up</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
    <p>
      Already have an account?
      <router-link to="/login">Log in here</router-link>.
    </p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RegisterView',
  data() {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  methods: {
    async doRegister() {
      this.error = ''
      try {
        await axios.post('/auth/register', {
          username: this.username,
          password: this.password
        })
        // On success, redirect to login
        this.$router.push('/login')
      } catch (e) {
        // Show server‐sent message or fallback
        this.error = e.response?.data?.msg || 'Registration failed'
      }
    }
  }
}
</script>

<style scoped>
.field { margin-bottom: 0.75em; }
.error { color: red; }
</style>
