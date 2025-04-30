<!-- src/components/FavouriteButton.vue -->
<script setup>
import { ref } from 'vue';
import api from '../api';

const props = defineProps({ profileId: Number });
const isFav = ref(false);

const toggle = async () => {
  if (!isFav.value) {
    await api.post('/favourites', { fav_user_id: props.profileId });
  }
  // you could also call DELETE if already fav’d…
  isFav.value = !isFav.value;
};
</script>

<template>
  <button @click="toggle">
    {{ isFav ? '★' : '☆' }}
  </button>
</template>
