# from frontend/src/views
cat > ProfileList.vue << 'EOF'
<template>
  <div style="max-width:800px; margin:auto; padding:1em;">
    <h2>Profiles</h2>
    <form @submit.prevent="searchProfiles" style="margin-bottom:1em;">
      <input v-model="filters.name" placeholder="Name" />
      <input v-model.number="filters.birth_year" placeholder="Birth Year" type="number" />
      <select v-model="filters.sex">
        <option value="">Sex</option>
        <option>Male</option>
        <option>Female</option>
      </select>
      <select v-model="filters.race">
        <option value="">Race</option>
        <option>African</option>
        <option>Asian</option>
        <option>European</option>
        <option>Other</option>
      </select>
      <button type="submit">Search</button>
      <button type="button" @click="loadRecent">Show Recent</button>
    </form>

    <ul>
      <li
        v-for="p in profiles"
        :key="p.id"
        style="border:1px solid #ccc; margin-bottom:0.5em; padding:0.5em;"
      >
        <strong>{{ p.user.username }}</strong> — {{ p.description }}<br />
        Parish: {{ p.parish }}, Age: {{ currentYear - p.birth_year }}<br />
        Sex: {{ p.sex }}, Race: {{ p.race }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProfileList',
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
        this.profiles = res.data.sort((a, b) => b.id - a.id).slice(0, 4)
      } catch (e) {
        console.error('Error loading recent profiles', e)
      }
    },
    async searchProfiles() {
      try {
        const params = {}
        if (this.filters.name) params.name = this.filters.name
        if (this.filters.birth_year) params.birth_year = this.filters.birth_year
        if (this.filters.sex) params.sex = this.filters.sex
        if (this.filters.race) params.race = this.filters.race
        const res = await axios.get('/search', { params })
        this.profiles = res.data
      } catch (e) {
        console.error('Error searching profiles', e)
      }
    }
  }
}
</script>
EOF
