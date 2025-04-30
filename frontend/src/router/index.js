import { createRouter, createWebHashHistory } from 'vue-router'

// Import the actual files under src/views/
import Home     from '../views/Home.vue'
import Login    from '../views/LoginView.vue'
import Register from '../views/RegisterView.vue'
import NotFound from '../views/NotFound.vue'

// Once you scaffold them, you can re-enable these from src/views or src/components:
// import ProfileList   from '../views/ProfileList.vue'
// import ProfileForm   from '../views/ProfileForm.vue'
// import ProfileDetail from '../views/ProfileDetail.vue'
// import FavouriteList from '../views/FavouriteList.vue'

const routes = [
  { path: '/',         component: Home },
  { path: '/login',    component: Login },
  { path: '/register', component: Register },
  // { path: '/profiles',       component: ProfileList,   meta: { requiresAuth: true } },
  // { path: '/create-profile', component: ProfileForm,   meta: { requiresAuth: true } },
  // { path: '/profiles/:id',   component: ProfileDetail, meta: { requiresAuth: true } },
  // { path: '/favourites',     component: FavouriteList, meta: { requiresAuth: true } },
  { path: '/:pathMatch(.*)*', component: NotFound }
]

export default createRouter({
  history: createWebHashHistory(),
  routes
})
