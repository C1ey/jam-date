<template>
  <div class="register-page">
    <h1>Register</h1>
    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label>Username</label>
        <input v-model="form.username" type="text" required />
      </div>

      <div class="form-group">
        <label>Full Name</label>
        <input v-model="form.name" type="text" required />
      </div>

      <div class="form-group">
        <label>Email</label>
        <input v-model="form.email" type="email" required />
      </div>

      <div class="form-group">
        <label>Password</label>
        <input v-model="form.password" type="password" required />
      </div>

      <div class="form-group">
        <label>Photo URL (optional)</label>
        <input v-model="form.photo" type="url" />
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
      form: {
        username: '',
        name:     '',
        email:    '',
        password: '',
        photo:    ''
      },
      error: ''
    };
  },
  methods: {
    async onSubmit() {
      this.error = '';
      try {
        // axios is already wired to VITE_API_URL
        await axios.post('/auth/register', this.form);
        this.$router.push('/login');
      } catch (e) {
        console.error(e.response?.data);
        this.error = e.response?.data?.msg || 'Registration failed';
      }
    }
  }
};
</script>

<style scoped>
.register-page {
  max-width: 400px;
  margin: 2rem auto;
}
.form-group {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.3rem;
}
input {
  width: 100%;
  padding: 0.5rem;
  box-sizing: border-box;
}
button {
  padding: 0.6rem 1.2rem;
}
.error {
  color: #e74c3c;
  margin-top: 0.8rem;
}
</style>
