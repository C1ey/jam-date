// src/router/index.js

import { createRouter, createWebHashHistory } from 'vue-router'

// your “page” components
import HomeView       from '../views/HomeView.vue'
import RegisterView   from '../views/RegisterView.vue'
import LoginView      from '../views/LoginView.vue'
import ProfileList    from '../views/ProfileList.vue'
import ProfileForm    from '../views/ProfileForm.vue'
import ProfileDetail  from '../views/ProfileDetail.vue'
import FavouriteList  from '../views/FavouriteList.vue'
import NotFound       from '../views/NotFound.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },

  // ——— PROFILES ——————————————————————————————
  {
    path: '/profiles',
    name: 'profiles',
    component: ProfileList,
    meta: { requiresAuth: true }
  },
  {
    path: '/create-profile',
    name: 'create-profile',
    component: ProfileForm,
    meta: { requiresAuth: true }
  },
  {
    path: '/profiles/:id',
    name: 'profile-detail',
    component: ProfileDetail,
    props: true,
    meta: { requiresAuth: true }
  },

  // ——— FAVOURITES —————————————————————————————
  {
    path: '/favourites',
    name: 'favourites',
    component: FavouriteList,
    meta: { requiresAuth: true }
  },

  // ——— CATCH-ALL 404 ————————————————————————————
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes
})

// (optional) protect those routes requiring login:
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !localStorage.getItem('jwt')) {
    return next('/login')
  }
  next()
})

export default router
