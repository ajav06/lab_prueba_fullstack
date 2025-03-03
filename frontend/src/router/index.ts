import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/SetsView.vue'),
    },
    {
      path: '/:setId/cards',
      name: 'CardsBySet',
      component: () => import('../views/CardsView.vue'),
    },
  ],
});

export default router;
