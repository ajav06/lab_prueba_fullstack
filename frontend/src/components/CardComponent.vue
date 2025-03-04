<script setup lang="ts">
import SpinnerLoading from './SpinnerLoading.vue';
import SvgIcon from './SvgIcon.vue';

interface Props {
  isLoading: boolean;
  title: string;
  modelValue?: string;
  withSearch?: boolean;
  goBack?: VoidFunction;
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
  <main class="container mx-auto rounded-2xl rounded-bl-[8rem] bg-gray-400 p-12 px-20">
    <spinner-loading v-if="props.isLoading" />
    <div v-else>
      <section class="mb-8 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <span
            class="flex size-24 items-center justify-center rounded-full border-8 border-gray-300 bg-tertiary"
          />

          <h1 class="text-xl font-bold text-gray-800">{{ props.title }}</h1>
        </div>
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
            placeholder="Buscar..."
            class="rounded-xl p-2 px-4 font-mono text-xl"
            :value="String(modelValue ?? '')"
            @input="handleInput($event)"
          />
        </div>
      </section>

      <slot name="content"> </slot>

      <div class="mt-8 flex justify-center" v-if="props.goBack">
        <button
          type="button"
          class="flex items-center gap-2 rounded-2xl bg-black px-4 py-2 text-gray-200"
          @click="props.goBack"
        >
          <svg-icon name="arrow-left" size="20" />
          Volver
        </button>
      </div>
    </div>
  </main>
</template>
