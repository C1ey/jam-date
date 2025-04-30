<!-- src/components/ProfileDetail.vue -->
<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import api from '../api';

const route   = useRoute();
const profile = ref(null);

onMounted(async () => {
  const { data } = await api.get(`/profiles/${route.params.id}`);
  profile.value = data;
});
</script>

<template>
  <div v-if="profile">
    <h2>{{ profile.username }}’s Profile</h2>
    <p>{{ profile.description }}</p>
    <p><strong>Parish:</strong> {{ profile.parish }}</p>
    <!-- etc… -->
  </div>
</template>
