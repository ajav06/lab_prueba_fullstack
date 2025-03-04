<script setup lang="ts">
import { useRouter } from 'vue-router';
import { onMounted, ref, type Ref } from 'vue';
import { type Set } from '@/models';
import { getSets } from '@/api/setApis';
import CardComponent from '@/components/CardComponent.vue';
import TableComponent from '@/components/TableComponent.vue';
import SvgIcon from '@/components/SvgIcon.vue';
import Tag from '@/components/Tag.vue';

const router = useRouter();
const sets: Ref<Set[]> = ref([]);
const loading: Ref<boolean> = ref(false);
const searchQuery: Ref<string> = ref('');
const headers = [
  { text: 'Nombre', field: 'name' },
  { text: 'Serie', field: 'series' },
  { text: 'Total de cartas', field: 'total' },
  { text: 'Código PTCGO', field: 'ptcgoCode' },
  { text: 'Logo', field: 'logoUrl' },
  { text: 'Fecha de lanzamiento', field: 'releaseDate' },
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

const formatDate = (date: string) =>
  new Date(date).toLocaleDateString('es-CL', { timeZone: 'UTC' });

onMounted(() => {
  fetchSets();
});
</script>

<template>
  <card-component :is-loading="loading" title="Sets de cartas" with-search v-model="searchQuery">
    <template #content>
      <TableComponent
        :headers="headers"
        :items="sets"
        :items-per-page="5"
        :search-query="searchQuery"
      >
        <template #total="{ value }">
          <span class="font-mono"> {{ value.total }} </span>
        </template>
        <template #ptcgoCode="{ value }">
          <Tag :text="value.ptcgoCode" />
        </template>
        <template #logoUrl="{ value }">
          <img :src="value.logoUrl" :alt="value.name" loading="lazy" class="max-h-16" />
        </template>
        <template #releaseDate="{ value }">
          <span class="text-sm font-mono">{{ formatDate(value.releaseDate) }}</span>
        </template>
        <template #actions="{ value }">
          <button
            type="button"
            class="mx-auto text-[0.8rem] flex items-center gap-1 bg-green-600 px-2 py-1 rounded-2xl"
            @click="router.push({ name: 'CardsBySet', params: { setId: value.id } })"
          >
            <svg-icon name="eye-fill" size="14" />
            Ver
          </button>
        </template>
      </TableComponent>
    </template>
  </card-component>
</template>
