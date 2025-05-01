<template>
  <div class="page">
    <h2>Profile Details</h2>

    <div v-if="loading">Loading…</div>

    <div v-else-if="profile">
      <!-- Photo -->
      <img
        v-if="profile.photo"
        :src="profile.photo"
        alt="Profile photo"
        class="profile-photo"
      />

      <!-- Basic Info -->
      <h3>{{ profile.user.name || profile.user.username }}</h3>
      <p><strong>Email:</strong> {{ profile.user.email }}</p>
      <p><strong>Age:</strong> {{ age }}</p>
      <p><strong>Height:</strong> {{ profile.height }}″</p>
      <p><strong>Parish:</strong> {{ profile.parish }}</p>
      <p><strong>Sex:</strong> {{ profile.sex }}</p>
      <p><strong>Race:</strong> {{ profile.race }}</p>

      <!-- Description & Bio -->
      <p><strong>Description:</strong> {{ profile.description }}</p>
      <p><strong>Biography:</strong> {{ profile.biography }}</p>

      <!-- Preferences -->
      <p><strong>Fav Cuisine:</strong> {{ profile.fav_cuisine || '—' }}</p>
      <p><strong>Fav Colour:</strong> {{ profile.fav_colour || '—' }}</p>
      <p><strong>Fav Subject:</strong> {{ profile.fav_school_subject || '—' }}</p>
      <p><strong>Political:</strong> {{ profile.political ? 'Yes' : 'No' }}</p>
      <p><strong>Religious:</strong> {{ profile.religious ? 'Yes' : 'No' }}</p>
      <p><strong>Family Oriented:</strong> {{ profile.family_oriented ? 'Yes' : 'No' }}</p>

      <!-- Actions -->
      <div class="actions">
        <button @click="emailProfile" class="btn">
          📧 Email Profile
        </button>
        <button @click="toggleFavourite" class="btn favourite">
          <span v-if="isFavourite">❤️</span>
          <span v-else>🤍</span>
          Favourite
        </button>
      </div>
    </div>

    <div v-else>
      <p class="error">Profile not found.</p>
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
      loading: true,
      isFavourite: false,
      error: ''
    }
  },
  computed: {
    age() {
      if (!this.profile) return '—'
      return new Date().getFullYear() - this.profile.birth_year
    }
  },
  async created() {
    try {
      const { id } = this.$route.params
      const res = await axios.get(`/profiles/${id}`)
      this.profile = res.data
      // optionally: check if already favourited by current user
      // const favs = await axios.get(`/users/${this.profile.user.id}/favourites`)
      // this.isFavourite = favs.data.some(f => f.fav_profile_id === this.profile.id)
    } catch (e) {
      this.error = e.response?.data?.msg || 'Could not load profile'
    } finally {
      this.loading = false
    }
  },
  methods: {
    emailProfile() {
      alert(`Pretend emailing ${this.profile.user.email}`)
    },
    async toggleFavourite() {
      this.error = ''
      try {
        await axios.post(`/profiles/${this.profile.id}/favourite`)
        this.isFavourite = true
      } catch (e) {
        this.error = e.response?.data?.msg || 'Could not add favourite'
      }
    }
  }
}
</script>

<style scoped>
.page {
  max-width: 600px;
  margin: auto;
  padding: 2em;
}
.profile-photo {
  display: block;
  width: 100%;
  max-width: 300px;
  border-radius: 8px;
  margin: 1em 0;
}
.actions {
  margin-top: 1.5em;
}
.btn {
  padding: 0.6em 1.2em;
  margin-right: 1em;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: #eee;
}
.btn:hover {
  background: #ddd;
}
.favourite span {
  margin-right: 0.5em;
}
.error {
  color: red;
  margin-top: 1em;
}
</style>
