<template>
  <div v-if="profile" class="profile-detail">
    <h2>{{ profile.user.name }} (@{{ profile.user.username }})</h2>
    <img v-if="profile.user.photo" :src="profile.user.photo" alt="Profile photo" class="photo"/>
    <p><strong>Email:</strong> {{ profile.user.email }}</p>
    <p><strong>Description:</strong> {{ profile.description }}</p>
    <!-- ...rest of your fields -->
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ProfileDetail',
  data() {
    return {
      profile: null,
      matches: [],
      currentYear: new Date().getFullYear()
    }
  },
  async created() {
    try {
      const res = await axios.get(`/profiles/${this.$route.params.id}`)
      this.profile = res.data
    } catch (e) {
      console.error(e)
    }
  },
  // ...methods unchanged
}
</script>

<style>
.profile-detail .photo {
  max-width: 150px;
  border-radius: 50%;
  margin-bottom: 1em;
}
</style>
