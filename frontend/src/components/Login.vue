<template>
  <div>
    <h1>🔐 Login</h1>
    <form @submit.prevent="doLogin">
      <input v-model="username" placeholder="Username" /><br/>
      <input v-model="password" type="password" placeholder="Password" /><br/>
      <button>Login</button>
    </form>
  </div>
</template>
<script>
export default {
  name: 'Login',
  data() {
    return { username: '', password: '' }
  },
  methods: {
    async doLogin() {
      // for now just console.log
      console.log('login', this.username, this.password)
    }
  }
}
</script>
