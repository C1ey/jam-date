<template>
  <div style="max-width:800px; margin:auto; padding:1em;">
    <h1>Welcome to Jam-Date</h1>

    <!-- SEARCH FORM -->
    <section style="margin-bottom:2em;">
      <h2>Find Your Match</h2>
      <form @submit.prevent="searchProfiles" style="display:flex; gap:0.5em; flex-wrap:wrap;">
        <input
          v-model="filters.name"
          placeholder="Name"
          style="flex:1; min-width:120px;"
        />
        <input
          v-model.number="filters.birth_year"
          type="number"
          placeholder="Birth Year"
          style="width:100px;"
        />
        <select v-model="filters.sex" style="width:120px;">
          <option value="">Sex</option>
          <option>Male</option>
          <option>Female</option>
        </select>
        <select v-model="filters.race" style="width:140px;">
          <option value="">Race</option>
          <option>African</option>
          <option>Asian</option>
          <option>European</option>
          <option>Other</option>
        </select>
        <button type="submit">Search</button>
        <button type="button" @click="loadRecent">Show Recent</button>
      </form>
    </section>

    <!-- PROFILES LIST -->
    <section>
      <h2 v-if="profiles.length">Profiles</h2>
      <p v-else>No profiles found.</p>
      <ul style="list-style:none; padding:0;">
        <li
          v-for="p in profiles"
          :key="p.id"
          style="border:1px solid #ccc; margin-bottom:1em; padding:1em; border-radius:4px;"
        >
          <router-link :to="`/profiles/${p.id}`" style="font-weight:bold;">
            {{ p.user.username }}
          </router-link>
          — {{ p.description }}<br>
          Parish: {{ p.parish }}, Age: {{ currentYear - p.birth_year }}<br>
          Sex: {{ p.sex }}, Race: {{ p.race }}
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      profiles: [],
      filters: { name: '', birth_year: null, sex: '', race: '' },
      currentYear: new Date().getFullYear()
    }
  },
  created() {
    this.loadRecent()
  },
  methods: {
    async loadRecent() {
      try {
        const res = await axios.get('/profiles')
        // take the 4 most recent profiles
        this.profiles = res.data
          .sort((a, b) => b.id - a.id)
          .slice(0, 4)
      } catch (err) {
        console.error('Failed to load recent profiles', err)
      }
    },
    async searchProfiles() {
      try {
        const params = {}
        if (this.filters.name)        params.name = this.filters.name
        if (this.filters.birth_year)  params.birth_year = this.filters.birth_year
        if (this.filters.sex)         params.sex = this.filters.sex
        if (this.filters.race)        params.race = this.filters.race

        const res = await axios.get('/search', { params })
        this.profiles = res.data
      } catch (err) {
        console.error('Search failed', err)
      }
    }
  }
}
</script>
