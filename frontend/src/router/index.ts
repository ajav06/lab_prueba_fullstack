import { createRouter, createWebHistory } from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Sets',
      component: () => import('../views/SetsView.vue'),
    },
    {
      path: '/:setId/cards',
      name: 'CardsBySet',
      component: () => import('../views/CardsView.vue'),
    },
    {
      path: '/:setId/cards/:cardId',
      name: 'CardDetails',
      component: () => import('../views/CardDetailsView.vue'),
    },
    {
      path: '/:pathMatch(.*)*',
      component: () => import('../views/NotFound.vue'),
    },
  ],
});

export default router;
