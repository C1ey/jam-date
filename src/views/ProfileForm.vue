<template>
  <div class="page">
    <h2>Create Profile</h2>
    <form @submit.prevent="onSubmit" enctype="multipart/form-data">
      <!-- text fields… -->
      <div><label>Description</label><input v-model="form.description" required /></div>
      <div><label>Parish</label><input v-model="form.parish" required /></div>
      <div><label>Biography</label><textarea v-model="form.biography" required /></div>
      <div><label>Sex</label><input v-model="form.sex" required /></div>
      <div><label>Race</label><input v-model="form.race" required /></div>
      <div><label>Birth Year</label><input v-model.number="form.birth_year" type="number" required /></div>
      <div><label>Height (inches)</label><input v-model.number="form.height" type="number" required /></div>

      <!-- new: file picker -->
      <div>
        <label>Photo</label>
        <input type="file" @change="onFileChange" accept="image/*" />
      </div>

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
      file: null,
      error: ''
    }
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0]
    },
    async onSubmit() {
      this.error = ''
      try {
        const formData = new FormData()
        // append text fields
        Object.entries(this.form).forEach(([k,v]) => {
          formData.append(k, v)
        })
        // append file if present
        if (this.file) {
          formData.append('photo', this.file)
        }
        const res = await axios.post('/profiles', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
        this.$router.push({ name: 'profile-detail', params: { id: res.data.id }})
      } catch (e) {
        this.error = e.response?.data?.msg || 'Could not create profile'
      }
    }
  }
}
</script>

<style scoped>
.page { padding: 2em; }
.error { color: red; margin-top: 1em; }
</style>
