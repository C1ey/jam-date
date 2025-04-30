<template>
  <div class="page">
    <h2>Profile Details</h2>
    <div v-if="profile">
      <p><strong>Description:</strong> {{ profile.description }}</p>
      <p><strong>Parish:</strong> {{ profile.parish }}</p>
      <p><strong>Biography:</strong> {{ profile.biography }}</p>
      <p><strong>Age:</strong> {{ new Date().getFullYear() - profile.birth_year }}</p>
      <button @click="addFavourite">❤️ Favourite</button>
    </div>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ProfileDetail',
  data() {
    return {
      profile: null,
      error: ''
    }
  },
  async created() {
    try {
      const res = await axios.get(`/profiles/${this.$route.params.id}`)
      this.profile = res.data
    } catch (e) {
      this.error = 'Could not load profile'
    }
  },
  methods: {
    async addFavourite() {
      try {
        await axios.post(`/profiles/${this.profile.id}/favourite`)
        alert('Added to favourites')
      } catch (e) {
        this.error = 'Could not add favourite'
      }
    }
  }
}
</script>

<style scoped>
.page { padding: 2em; }
.error { color: red; margin-top: 1em; }
</style>
