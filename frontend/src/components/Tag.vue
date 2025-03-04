<script setup lang="ts">
const props = defineProps<{
  text: string;
}>();
</script>

<template>
  <span
    class="max-h-[1.25rem] flex-shrink-0 rounded bg-secondary px-2 py-1 text-[0.625rem] font-bold uppercase leading-normal"
  >
    {{ props.text }}
  </span>
</template>
