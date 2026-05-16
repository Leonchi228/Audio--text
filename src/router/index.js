import { createRouter, createWebHistory } from 'vue-router'


import Main from '../views/Main.vue'


const routes = [
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/',
    name: 'main',
    component: Main
  },
  {
    path: '/reset-password',
    name: 'reset-password',
    component: () => import('../views/ResetPassword.vue')
  },
  {
    path: '/update-password',
    name: 'update-password',
    component: () => import('../views/UpdatePassword.vue')
  },
  {
    path: '/wait-email',
    name: 'wait-email',
    component: () => import('../views/WaitEmail.vue')
  },
  {
    path:'/private',
    name:'private',
    component:()=>import('../views/Private.vue')
  },
    {
    path:'/doc',
    name:'documentation',
    component:()=>import('../views/Documentation.vue')
  }
]


const router = createRouter({
  history: createWebHistory(), 
  routes
})

export default router