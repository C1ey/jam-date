<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const profiles = ref([])
const loading  = ref(true)
const search   = ref('')

const displayed = computed(() => {
  const term = search.value.toLowerCase().trim()
  let list = profiles.value
  if (term) {
    list = list.filter(p =>
      [p.user.name, p.description, p.sex, p.race, p.birth_year]
        .some(f => f && f.toString().toLowerCase().includes(term))
    )
  }
  return list.slice(0,4)
})

onMounted(async () => {
  try {
    const res = await axios.get('/profiles')
    profiles.value = res.data
  } catch {
    console.error('Could not load profiles')
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="home-page">
    <h2>Welcome to Jam-Date</h2>
    <h3>Find Your Match</h3>
    <div class="search-bar">
      <input v-model="search" placeholder="Search…" />
    </div>
    <div v-if="loading">Loading…</div>
    <div v-else-if="displayed.length">
      <div class="grid">
        <div v-for="p in displayed" :key="p.id" class="card">
          <img :src="p.photo" alt="" v-if="p.photo"/>
          <h4>{{ p.user.name }}</h4>
          <p>{{ p.description }}</p>
          <router-link :to="`/profiles/${p.id}`">View Details →</router-link>
        </div>
      </div>
    </div>
    <div v-else>No profiles found.</div>
  </div>
</template>

<style scoped>
.home-page { max-width:800px; margin:auto; padding:1em }
.search-bar input { width:100%; padding:.5em; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(200px,1fr)); gap:1em; }
.card { border:1px solid #ccc; padding:.5em; text-align:center; }
.card img { width:100%; height:120px; object-fit:cover; border-radius:4px; }
</style>
