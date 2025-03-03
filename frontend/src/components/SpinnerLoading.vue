<script setup lang="ts"></script>

<template>
  <p class="spinner mx-auto"></p>
</template>

<style lang="scss" scoped>
.spinner {
  @apply size-20 animate-spin rounded-full border-8 border-solid border-primary border-t-primary;

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
}
</style>
