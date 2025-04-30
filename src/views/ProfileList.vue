<template>
  <div class="page">
    <h2>All Profiles</h2>
    <ul>
      <li v-for="profile in profiles" :key="profile.id">
        <router-link :to="{ name: 'profile-detail', params: { id: profile.id }}">
          {{ profile.description }} ({{ profile.sex }}, {{ profile.parish }})
        </router-link>
      </li>
    </ul>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ProfileList',
  data() {
    return {
      profiles: [],
      error: ''
    }
  },
  async created() {
    try {
      const res = await axios.get('/profiles')
      this.profiles = res.data
    } catch (e) {
      this.error = 'Could not load profiles'
    }
  }
}
</script>

<style scoped>
.page { padding: 2em; }
.error { color: red; margin-top: 1em; }
</style>
