<script setup lang="ts">
import { useRouter } from 'vue-router';
import CardComponent from '@/components/CardComponent.vue';

const router = useRouter();
</script>

<template>
  <card-component
    :is-loading="false"
    :title="'Página no encontrada'"
    :go-back="() => router.push({ name: 'Sets' })"
    with-search
  >
  </card-component>
</template>
