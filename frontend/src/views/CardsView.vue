<script setup lang="ts">
import { useRoute } from 'vue-router';
import { onMounted, ref, type Ref } from 'vue';
import { Card } from '@/models';
import { getCardsBySet } from '@/api/apiSets';
import CardComponent from '@/components/CardComponent.vue';
import TableComponent from '@/components/TableComponent.vue';
import SvgIcon from '@/components/SvgIcon.vue';

const route = useRoute();
const cards: Ref<Card[]> = ref([]);
const loading: Ref<boolean> = ref(false);
const searchQuery: Ref<string> = ref('');
const headers = [
  { text: 'Nombre', field: 'name' },
  { text: 'Super tipos', field: 'supertype' },
  { text: 'Sub tipos', field: 'subtypes' },
  { text: 'Tipos', field: 'types' },
  { text: 'Número', field: 'number' },
  { text: 'Rareza', field: 'rarity' },
  { text: 'Cartas', field: 'actions' },
];

const fetchSets = async () => {
  try {
    loading.value = true;
    const response = await getCardsBySet(String(route.params.setId));
    cards.value = response.results;
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
  <card-component :is-loading="loading" title="Cartas" with-search v-model="searchQuery">
    <template #content>
      <TableComponent
        :headers="headers"
        :items="cards"
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
    </template>
  </card-component>
</template>
