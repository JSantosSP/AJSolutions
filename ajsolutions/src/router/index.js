import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'homeView',
        component: () => import('../views/HomeView.vue')
    },
    {
        path: '/piezas',
        name: 'piezasView',
        component: () => import('../views/PiezasView.vue')
    },
    {
        path: '/piezas/view/:nombre',
        name: 'viewPieza',
        component: () => import('../views/ViewPieza.vue')
    },
    {
        path: '/3d',
        name: '3dView',
        component: () => import('../views/3DView.vue')
    },
    {
        path: '/animaciones',
        name: 'animacionesView',
        component: () => import('../views/AnimacionesView.vue')
    }
  ]
  
  const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })

export default router