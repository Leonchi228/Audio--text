import { createRouter, createWebHistory } from 'vue-router'


import RegisterView from '../views/Register.vue'
import LoginView from '../views/Login.vue'


const routes = [
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/login',
    name: 'login',
    component:LoginView
  },
  {
    path: '/',
    name: 'main',
    component: () => import('../views/Main.vue')
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
  }
]


const router = createRouter({
  history: createWebHistory(), 
  routes
})

export default router