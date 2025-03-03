<script setup lang="ts">
import SpinnerLoading from './SpinnerLoading.vue';

interface Props {
  isLoading: boolean;
  title: string;
  modelValue: string;
  withSearch?: boolean;
}

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void;
}>();

const handleInput = ($event: Event) => {
  const target = $event.target as HTMLInputElement;
  emit('update:modelValue', String(target.value));
};

const props = defineProps<Props>();
</script>

<template>
  <main class="container mx-auto p-12 px-20 bg-gray-400 rounded-2xl rounded-bl-[8rem]">
    <spinner-loading v-if="props.isLoading" />
    <div v-else>
      <section class="mb-8 flex justify-between items-center">
        <h1 class="text-gray-800 text-2xl font-bold">{{ props.title }}</h1>
        <div class="flex items-center gap-3">
          <div class="size-9 rounded-full bg-primary-dark"></div>
          <div class="size-9 rounded-full bg-secondary"></div>
          <div class="size-9 rounded-full bg-green-600"></div>
          <label for="search"></label>
          <input
            v-if="props.withSearch"
            type="text"
            name="search"
            id="search"
            placeholder="Buscar set..."
            class="text-xl rounded-xl p-2 px-4"
            :value="String(modelValue ?? '')"
            @input="handleInput($event)"
          />
        </div>
      </section>

      <slot name="content"> </slot>
    </div>
  </main>
</template>
