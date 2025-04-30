<template>
  <div class="page">
    <h2>Create Profile</h2>
    <form @submit.prevent="onSubmit">
      <div><label>Description</label><input v-model="form.description" required /></div>
      <div><label>Parish</label><input v-model="form.parish" required /></div>
      <div><label>Biography</label><textarea v-model="form.biography" required /></div>
      <div><label>Sex</label><input v-model="form.sex" required /></div>
      <div><label>Race</label><input v-model="form.race" required /></div>
      <div><label>Birth Year</label><input v-model.number="form.birth_year" type="number" required /></div>
      <div><label>Height (inches)</label><input v-model.number="form.height" type="number" required /></div>
      <div><label>Favorite Cuisine</label><input v-model="form.fav_cuisine" /></div>
      <div><label>Favorite Colour</label><input v-model="form.fav_colour" /></div>
      <div><label>Favorite School Subject</label><input v-model="form.fav_school_subject" /></div>
      <div><label>Political</label><input type="checkbox" v-model="form.political" /></div>
      <div><label>Religious</label><input type="checkbox" v-model="form.religious" /></div>
      <div><label>Family Oriented</label><input type="checkbox" v-model="form.family_oriented" /></div>
      <button type="submit">Submit</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ProfileForm',
  data() {
    return {
      form: {
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
        family_oriented: false
      },
      error: ''
    }
  },
  methods: {
    async onSubmit() {
      this.error = ''
      try {
        const res = await axios.post('/profiles', this.form)
        this.$router.push({ name: 'profile-detail', params: { id: res.data.id }})
      } catch (e) {
        this.error = 'Could not create profile'
      }
    }
  }
}
</script>

<style scoped>
.page { padding: 2em; }
.error { color: red; margin-top: 1em; }
</style>
