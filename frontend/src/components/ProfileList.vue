<!-- src/components/ProfileList.vue -->
<script setup>
import { ref, onMounted } from 'vue';
import api from '../api';
import FavouriteButton from './FavouriteButton.vue';

const profiles = ref([]);

onMounted(async () => {
  const { data } = await api.get('/profiles');
  profiles.value = data;
});
</script>

<template>
  <div>
    <h2>All Profiles</h2>
    <ul>
      <li v-for="p in profiles" :key="p.id">
        <router-link :to="`/profiles/${p.id}`">{{ p.username }}</router-link>
        <FavouriteButton :profileId="p.id" />
      </li>
    </ul>
  </div>
</template>
