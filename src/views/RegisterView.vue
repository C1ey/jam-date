<template>
  <div class="auth-page">
    <h2>Register</h2>
    <form @submit.prevent="onRegister">
      <div>
        <label for="username">Username</label><br>
        <input
          id="username"
          v-model="username"
          type="text"
          placeholder="Choose a username"
          required
        />
      </div>
      <div style="margin-top:0.5em;">
        <label for="password">Password</label><br>
        <input
          id="password"
          v-model="password"
          type="password"
          placeholder="Choose a password"
          required
        />
      </div>
      <button type="submit" style="margin-top:1em;">Sign Up</button>
    </form>

    <p v-if="error" class="error">{{ error }}</p>
    <p style="margin-top:1em;">
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
    async onRegister() {
      this.error = ''
      try {
        await axios.post('/auth/register', {
          username: this.username,
          password: this.password
        })
        // after successful register, send them to login
        this.$router.push({ name: 'login' })
      } catch (e) {
        this.error = e.response?.data?.msg || 'Registration failed'
      }
    }
  }
}
</script>

<style scoped>
.auth-page { max-width: 400px; margin: 2em auto; }
.error { color: red; margin-top: 1em; }
</style>
