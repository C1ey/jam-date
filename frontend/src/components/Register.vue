<template>
  <div>
    <h1>📝 Register</h1>
    <form @submit.prevent="doRegister">
      <input v-model="username" placeholder="Username" /><br/>
      <input v-model="password" type="password" placeholder="Password" /><br/>
      <button>Register</button>
    </form>
  </div>
</template>
<script>
export default {
  name: 'Register',
  data() {
    return { username: '', password: '' }
  },
  methods: {
    async doRegister() {
      console.log('register', this.username, this.password)
    }
  }
}
</script>
