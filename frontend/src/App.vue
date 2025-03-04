<script setup lang="ts">
import { ref, type Ref } from 'vue';
import NavBar from '@/components/NavBar.vue';
import InformationModal from '@/components/InformationModal.vue';

const visibleModal: Ref<boolean> = ref(false);
</script>

<template>
  <main class="mx-auto flex h-screen max-w-7xl items-center px-4 sm:px-6 lg:px-8">
    <nav-bar
      @open-modal="
        () => {
          visibleModal = true;
        }
      "
    />
    <RouterView />
    <information-modal
      :visible="visibleModal"
      @close="
        () => {
          visibleModal = false;
        }
      "
    />
  </main>
</template>
