<template>
  <div class="list-container">
    <h2>All Profiles</h2>

    <div v-if="loading">Loading…</div>
    <div v-else>
      <div v-if="profiles.length === 0">
        No profiles yet.
        <router-link to="/create-profile">Create the first one.</router-link>
      </div>

      <ul v-else class="profiles">
        <li
          v-for="p in profiles"
          :key="p.id"
          class="profile-item"
        >
          <img
            v-if="p.photo"
            :src="p.photo"
            alt="Profile photo"
            class="thumbnail"
          />
          <div class="info">
            <strong>{{ p.user.username }}</strong>
            — {{ p.description }}
            <router-link :to="`/profiles/${p.id}`" class="detail-link">
              View Details
            </router-link>
          </div>
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
.list-container {
  max-width: 800px;
  margin: auto;
  padding: 1em;
}
.profiles {
  list-style: none;
  padding: 0;
}
.profile-item {
  display: flex;
  align-items: center;
  border-bottom: 1px solid #ddd;
  padding: 0.5em 0;
}
.thumbnail {
  width: 80px;
  height: 80px;
  object-fit: cover;
  border-radius: 4px;
  margin-right: 1em;
}
.info {
  flex: 1;
}
.detail-link {
  margin-left: 1em;
}
.error {
  color: red;
  margin-top: 1em;
}
</style>
