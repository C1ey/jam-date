// frontend/src/router/index.js

import { createRouter, createWebHashHistory } from 'vue-router'

// “Page-level” views live in src/views
import Home     from '../views/Home.vue'
import Login    from '../views/LoginView.vue'
import Register from '../views/RegisterView.vue'
import NotFound from '../views/NotFound.vue'

// All of your actual feature components live in src/components
import ProfileList   from '../components/ProfileList.vue'
import ProfileForm   from '../components/ProfileForm.vue'
import ProfileDetail from '../components/ProfileDetail.vue'
import FavouriteList from '../components/FavouriteList.vue'

const routes = [
  { path: '/',                component: Home },
  { path: '/login',           component: Login },
  { path: '/register',        component: Register },

  // these require the user to be logged in
  { path: '/profiles',        component: ProfileList,   meta: { requiresAuth: true } },
  { path: '/create-profile',  component: ProfileForm,   meta: { requiresAuth: true } },
  { path: '/profiles/:id',    component: ProfileDetail, meta: { requiresAuth: true } },
  { path: '/favourites',      component: FavouriteList, meta: { requiresAuth: true } },

  // catch-all 404
  { path: '/:pathMatch(.*)*', component: NotFound }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !localStorage.getItem('jwt')) {
    return next('/login')
  }
  next()
})

export default router
