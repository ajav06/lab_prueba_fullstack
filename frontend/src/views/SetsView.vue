<script setup lang="ts">
import { onMounted, ref, type Ref } from 'vue';
import { Set } from '@/models';
import { getSets } from '@/api/apiSets';
import SpinnerLoading from '@/components/SpinnerLoading.vue';
import TableComponent from '@/components/TableComponent.vue';
import SvgIcon from '@/components/SvgIcon.vue';

const sets: Ref<Set[]> = ref([]);
const loading: Ref<boolean> = ref(false);
const searchQuery: Ref<string> = ref('');
const headers = [
  { text: 'Nombre', field: 'name' },
  { text: 'Serie', field: 'series' },
  { text: 'Total de Cartas', field: 'total' },
  { text: 'Código PTCGO', field: 'ptcgoCode' },
  { text: 'Logo', field: 'logoUrl' },
  { text: 'Fecha de Lanzamiento', field: 'releaseDate' },
  { text: 'Última Actualización', field: 'updatedAt' },
  { text: 'Cartas', field: 'actions' },
];

const fetchSets = async () => {
  try {
    loading.value = true;
    const response = await getSets();
    sets.value = response.results;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchSets();
});
</script>

<template>
  <main class="container mx-auto p-12 px-20 bg-gray-400 rounded-2xl rounded-bl-[8rem]">
    <SpinnerLoading v-if="loading" />
    <div v-else>
      <section class="mb-8 flex justify-between items-center">
        <h1 class="text-gray-800 text-2xl font-bold">Sets de cartas</h1>
        <div class="flex items-center gap-3">
          <div class="size-9 rounded-full bg-primary-dark"></div>
          <div class="size-9 rounded-full bg-secondary"></div>
          <div class="size-9 rounded-full bg-green-600"></div>
          <label for="search"></label>
          <input
            type="text"
            name="search"
            id="search"
            placeholder="Buscar set..."
            class="text-xl rounded-xl p-2 px-4"
            v-model="searchQuery"
          />
        </div>
      </section>

      <TableComponent
        :headers="headers"
        :items="sets"
        :items-per-page="5"
        :search-query="searchQuery"
      >
        <template #ptcgoCode="{ value }">
          <span
            class="bg-secondary max-h-[1.25rem] max-w-[3.75rem] flex-shrink-0 truncate rounded px-2 py-1 text-[0.625rem] font-bold uppercase leading-normal"
          >
            {{ value.ptcgoCode }}
          </span>
        </template>
        <template #logoUrl="{ value }">
          <img :src="value.logoUrl" :alt="value.name" loading="lazy" class="max-h-16" />
        </template>
        <template #actions="{ value }">
          <button
            type="button"
            class="mx-auto text-sm flex items-center gap-1 bg-tertiary p-2 rounded-2xl"
          >
            <svg-icon name="eye-fill" size="16" svg-class="text-tertiary-dark" />
            Ver
          </button>
        </template>
      </TableComponent>
    </div>
  </main>
</template>
