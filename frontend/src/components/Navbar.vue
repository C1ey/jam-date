<!-- src/components/Navbar.vue -->
<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const loggedIn = computed(() => !!localStorage.getItem('jwt'));

const logout = () => {
  localStorage.removeItem('jwt');
  router.push('/login');
};
</script>

<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/profiles">Profiles</router-link>
    <router-link v-if="!loggedIn" to="/login">Login</router-link>
    <router-link v-if="!loggedIn" to="/register">Register</router-link>
    <button v-if="loggedIn" @click="logout">Logout</button>
  </nav>
</template>
