<template>
  <div class="register-page">
    <h1>Register</h1>
    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label for="username">Username</label>
        <input id="username" v-model="username" type="text" placeholder="Kevin" required />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input id="password" v-model="password" type="password" placeholder="••••••" required />
      </div>

      <!-- NEW -->
      <div class="form-group">
        <label for="name">Full Name</label>
        <input id="name" v-model="name" type="text" placeholder="Kevin Smith" required />
      </div>

      <!-- NEW -->
      <div class="form-group">
        <label for="email">Email</label>
        <input id="email" v-model="email" type="email" placeholder="you@example.com" required />
      </div>

      <button type="submit">Sign Up</button>

      <p v-if="error" class="error">{{ error }}</p>
      <p>
        Already have an account?
        <router-link to="/login">Log in here.</router-link>
      </p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterView',
  data() {
    return {
      username: '',
      password: '',
      name: '',
      email: '',
      error: ''
    };
  },
  methods: {
    async onSubmit() {
      this.error = '';
      console.log('📤 Register payload:', {
        username: this.username,
        password: this.password,
        name:     this.name,
        email:    this.email
      });
      try {
        await axios.post('/auth/register', {
          username: this.username,
          password: this.password,
          name:     this.name,
          email:    this.email
        });
        this.$router.push('/login');
      } catch (err) {
        console.error('❌ register error:', err.response?.data);
        this.error = err.response?.data?.msg || 'Registration failed';
      }
    }
  }
};
</script>

<style scoped>
.register-page { max-width:400px; margin:2rem auto; }
.form-group { margin-bottom:1rem; }
label { display:block; margin-bottom:.3rem; }
input { width:100%; padding:.5rem; box-sizing:border-box; }
button { padding:.6rem 1.2rem; margin-top:1rem; }
.error { color:#e74c3c; margin-top:.8rem; }
</style>
