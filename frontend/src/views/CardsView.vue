<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref, type Ref } from 'vue';
import { type Card, type Set } from '@/models';
import { getCardsBySet } from '@/api/setApis';
import { getTypeColor } from '@/helpers';
import CardComponent from '@/components/CardComponent.vue';
import TableComponent from '@/components/TableComponent.vue';
import SvgIcon from '@/components/SvgIcon.vue';
import Tag from '@/components/Tag.vue';

const route = useRoute();
const router = useRouter();
const set: Ref<Set> = ref({} as Set);
const cards: Ref<Card[]> = ref([]);
const loading: Ref<boolean> = ref(false);
const searchQuery: Ref<string> = ref('');
const headers = [
  { text: 'Nombre', field: 'name' },
  { text: 'Categoría', field: 'supertype' },
  { text: 'Sub tipos', field: 'subtypes' },
  { text: 'Tipos', field: 'types' },
  { text: 'Número', field: 'number' },
  { text: 'Rareza', field: 'rarity' },
  { text: 'Cartas', field: 'actions' },
];

const fetchCards = async () => {
  try {
    loading.value = true;
    const response = await getCardsBySet(String(route.params.setId));
    set.value = response.results;
    cards.value = response.results.cards as Card[];
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchCards();
});
</script>

<template>
  <card-component
    :is-loading="loading"
    :title="`Cartas: ${set.name}`"
    :go-back="() => router.push({ name: 'Sets' })"
    with-search
    v-model="searchQuery"
  >
    <template #content>
      <TableComponent
        :headers="headers"
        :items="cards"
        :items-per-page="6"
        :search-query="searchQuery"
      >
        <template #supertype="{ value }">
          <Tag class="!bg-primary text-gray-100" :text="value.supertype" />
        </template>

        <template #subtypes="{ value }">
          <div class="flex flex-wrap gap-2">
            <Tag :text="subtype" v-for="(subtype, id) in value.subtypes" :key="id" />
          </div>
        </template>

        <template #types="{ value }">
          <div class="flex flex-wrap gap-2">
            <Tag
              :class="getTypeColor(type)"
              :text="type"
              v-for="(type, id) in value.types"
              :key="id"
            />
            <span v-if="!value.types?.length" class="font-mono">-</span>
          </div>
        </template>

        <template #number="{ value }">
          <span class="font-mono">
            {{ `${String(value.number).padStart(String(set?.total).length, '0')}/${set?.total}` }}
          </span>
        </template>

        <template #rarity="{ value }">
          <span v-if="value.rarity" class="font-mono">{{ value.rarity }}</span>
          <span v-else class="font-mono">-</span>
        </template>

        <template #actions="{ value }">
          <button
            type="button"
            class="mx-auto text-[0.8rem] flex items-center gap-1 bg-green-600 px-2 py-1 rounded-2xl"
            @click="
              () =>
                router.push({ name: 'CardDetails', params: { setId: set.id, cardId: value.id } })
            "
          >
            <svg-icon name="eye-fill" size="14" />
            Ver
          </button>
        </template>
      </TableComponent>
    </template>
  </card-component>
</template>
