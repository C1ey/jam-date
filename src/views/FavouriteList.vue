<template>
  <div class="page">
    <h2>My Favourites</h2>
    <ul>
      <li v-for="fav in favourites" :key="fav.id">
        User ID: {{ fav.fav_user_id }} – favourited at {{ fav.timestamp }}
      </li>
    </ul>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'FavouriteList',
  data() {
    return {
      favourites: [],
      error: ''
    }
  },
  async created() {
    try {
      const me = JSON.parse(atob(localStorage.getItem('jwt').split('.')[1])).sub
      const res = await axios.get(`/users/${me}/favourites`)
      this.favourites = res.data
    } catch (e) {
      this.error = 'Could not load favourites'
    }
  }
}
</script>

<style scoped>
.page { padding: 2em; }
.error { color: red; margin-top: 1em; }
</style>
