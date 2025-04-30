<template>
  <div style="max-width:800px; margin:auto; padding:1em;">
    <h2>All Profiles</h2>

    <div v-if="loading">Loading…</div>
    <div v-else>
      <div v-if="profiles.length === 0">
        No profiles yet. 
        <router-link to="/create-profile">Create the first one.</router-link>
      </div>

      <ul v-else>
        <li
          v-for="p in profiles"
          :key="p.id"
          style="border-bottom:1px solid #ddd; padding:0.5em 0;"
        >
          <strong>{{ p.user.username }}</strong>
          — {{ p.description }}
          <router-link :to="`/profiles/${p.id}`" style="margin-left:1em;">
            View Details
          </router-link>
        </li>
      </ul>
    </div>

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
      loading: true,
      error: ''
    }
  },
  async created() {
    try {
      const res = await axios.get('/profiles')
      this.profiles = res.data
    } catch (e) {
      this.error = e.response?.data?.msg || 'Could not load profiles'
    } finally {
      this.loading = false
    }
  }
}
</script>

<style scoped>
.error { color: red; margin-top: 1em; }
</style>
