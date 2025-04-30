<!-- src/components/FavouriteList.vue -->
<script setup>
import { ref, onMounted } from 'vue';
import api from '../api';

const favs = ref([]);

onMounted(async () => {
  const { data } = await api.get('/users/me/favourites');
  favs.value = data;  // assume your endpoint returns full profile objects
});
</script>

<template>
  <div>
    <h2>My Favourites</h2>
    <ul>
      <li v-for="p in favs" :key="p.id">
        <router-link :to="`/profiles/${p.id}`">{{ p.username }}</router-link>
      </li>
    </ul>
  </div>
</template>
