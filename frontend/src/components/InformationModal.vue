<script setup lang="ts">
import SvgIcon from './SvgIcon.vue';

const props = defineProps<{
  visible: boolean;
}>();

const emits = defineEmits<{
  (e: 'close'): void;
}>();
</script>

<template>
  <main v-if="props.visible">
    <div
      tabindex="-1"
      class="fixed inset-0 left-0 right-0 top-0 z-40 max-h-full w-full items-center justify-center overflow-y-auto overflow-x-hidden bg-black opacity-70"
      @click="emits('close')"
    ></div>

    <div
      class="fixed bottom-0 right-1/2 z-50 max-h-full w-full translate-x-1/2 landscape:bottom-1/2 landscape:max-w-xl landscape:translate-y-1/2"
    >
      <div
        class="relative rounded-t-[1.875rem] bg-gray-400 p-8 shadow landscape:rounded-2xl landscape:p-8"
      >
        <header class="mb-6 flex w-full items-center justify-between">
          <h3 class="text-neutral-dark text-2xl font-bold">Información adicional</h3>

          <button
            type="button"
            @click="emits('close')"
            class="text-neutral-dark flex items-center justify-center rounded-lg bg-transparent p-1 hover:bg-gray-500 hover:text-gray-700"
          >
            <span class="sr-only">Close</span>
            <svg-icon name="x-lg" size="20" />
          </button>
        </header>

        <hr class="mb-4 text-neutral-200" />

        <section class="max-h-[30rem] overflow-hidden overflow-y-auto text-left">
          <slot name="body">
            <div class="mb-4 flex flex-col gap-4">
              <p>
                <span class="font-semibold">{{ 'Desarrollado por: ' }}</span>
                <a
                  href="https://www.linkedin.com/in/ajav06/"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="text-white hover:text-gray-300"
                >
                  {{ 'Albert Acevedo' }}
                </a>
              </p>

              <p>
                <span class="font-semibold">{{ 'Contacto: ' }}</span>
                <a href="mailto:albert06@gmail.com" class="text-white hover:text-gray-300">
                  {{ 'albert06@gmail.com' }}
                </a>
              </p>

              <p>
                <span class="font-semibold">{{ 'Versión: ' }}</span>
                <span class="font-mono">{{ '1.0.0' }}</span>
              </p>
            </div>
          </slot>
        </section>
      </div>
    </div>
  </main>
</template>
