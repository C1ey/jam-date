<!-- src/components/ProfileForm.vue -->
<script setup>
import { reactive } from 'vue';
import api from '../api';
import { useRouter } from 'vue-router';

const form = reactive({
  description: '',
  parish: '',
  biography: '',
  sex: '',
  race: '',
  birth_year: null,
  height: null,
  fav_cuisine: '',
  fav_colour: '',
  fav_school_subject: '',
  political: false,
  religious: false,
  family_oriented: false,
});

const router = useRouter();

const submit = async () => {
  await api.post('/profiles', form);
  router.push('/profiles');
};
</script>

<template>
  <form @submit.prevent="submit">
    <h2>Create Your Profile</h2>
    <textarea v-model="form.description" placeholder="About you" required />
    <input v-model="form.parish" placeholder="Parish" required />
    <!-- add other fields similarly… -->
    <label><input type="checkbox" v-model="form.political" /> Political</label>
    <button type="submit">Save Profile</button>
  </form>
</template>
