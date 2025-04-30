<!-- frontend/src/App.vue -->
<template>
  <div id="app">
    <nav
      style="padding:1em; border-bottom:1px solid #ccc; display:flex; justify-content:space-between; align-items:center;"
    >
      <div>
        <router-link to="/">Home</router-link> |
        <router-link to="/register">Register</router-link> |
        <router-link to="/login">Login</router-link>
      </div>
      <!-- Theme switcher -->
      <ThemeToggle />
    </nav>
    <router-view/>
  </div>
</template>

<script>
import ThemeToggle from './components/ThemeToggle.vue'

export default {
  name: 'App',
  components: { ThemeToggle }
}
</script>

<style>
/* Light theme variables */
:root {
  --bg-color: #ffffff;
  --text-color: #000000;
}
/* Dark theme variables */
[data-theme="dark"] {
  --bg-color: #1a1a1a;
  --text-color: #f5f5f5;
}

/* Apply globally */
html, body, #app {
  background-color: var(--bg-color);
  color: var(--text-color);
  transition: background-color .3s, color .3s;
}
a {
  color: var(--text-color);
  text-decoration: none;
}
a.router-link-active {
  font-weight: bold;
  text-decoration: underline;
}
</style>
