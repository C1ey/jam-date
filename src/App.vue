<template>
  <div :class="theme">
    <nav class="navbar">
      <router-link to="/">Home</router-link>
      <template v-if="!loggedIn">
        | <router-link to="/register">Register</router-link>
        | <router-link to="/login">Login</router-link>
      </template>
      <template v-else>
        | <router-link to="/profiles">All Profiles</router-link>
        | <router-link to="/create-profile">Create Profile</router-link>
        | <router-link to="/favourites">Favourites</router-link>
        | <a href="#" @click.prevent="logout">Logout</a>
      </template>
      <button @click="toggleTheme">{{ theme==='light'?'🌙 Dark':'☀️ Light' }}</button>
    </nav>
    <router-view/>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const router   = useRouter()
const theme    = ref(localStorage.getItem('theme')||'light')
const loggedIn = ref(!!localStorage.getItem('jwt'))
document.documentElement.setAttribute('data-theme', theme.value)

function toggleTheme(){
  theme.value = theme.value==='light'?'dark':'light'
  document.documentElement.setAttribute('data-theme', theme.value)
  localStorage.setItem('theme', theme.value)
}

function logout(){
  localStorage.removeItem('jwt')
  loggedIn.value = false
  router.push('/login')
}
</script>

<style>
.navbar { padding:1em; background:#222; color:#fff; }
.navbar a { color:#0af; margin:0 .5em; text-decoration:none; }
</style>
