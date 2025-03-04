<script setup lang="ts">
import SvgIcon from './SvgIcon.vue';

const emits = defineEmits<{
  (e: 'open-modal'): void;
}>();
</script>

<template>
  <nav class="fixed left-0 z-10 rounded-r-2xl bg-black p-4 shadow-md">
    <ul class="flex flex-col gap-4">
      <li>
        <router-link to="/" class="flex flex-col items-center gap-1 text-sm text-gray-200">
          <svg-icon name="pokeball" size="22" svg-class="!text-gray-200" />
          <span>Inicio</span>
        </router-link>
      </li>
      <li>
        <button
          type="button"
          @click="emits('open-modal')"
          class="flex flex-col items-center gap-1 text-sm text-gray-200"
        >
          <svg-icon name="person" size="22" />
          <span>Contacto</span>
        </button>
      </li>
    </ul>
  </nav>
</template>
