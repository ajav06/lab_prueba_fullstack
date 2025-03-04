<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref, type Ref } from 'vue';
import { type Card } from '@/models';
import CardComponent from '@/components/CardComponent.vue';
import SvgIcon from '@/components/SvgIcon.vue';
import Tag from '@/components/Tag.vue';
import getCardById from '@/api/cardApis';
import { getTypeColor } from '@/helpers';

const route = useRoute();
const router = useRouter();
const card: Ref<Card> = ref({} as Card);
const loading: Ref<boolean> = ref(false);

const fetchCard = async () => {
  try {
    loading.value = true;
    const response = await getCardById(String(route.params.cardId));
    card.value = response.results;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
};

const openWeb = (url: string) => {
  window.open(url, '_blank');
};

onMounted(() => {
  fetchCard();
});
</script>

<template>
  <card-component
    :is-loading="loading"
    :title="card.name || ''"
    :go-back="() => router.push({ name: 'CardsBySet', params: { setId: card.setId } })"
  >
    <template #content>
      <section
        v-if="card?.id"
        class="flex gap-20 bg-gray-50 rounded-xl max-h-[26rem] px-6 py-12 justify-center"
      >
        <img
          :src="card.images?.find(({ type }) => type === 'small')?.url"
          :alt="card.name"
          class="max-h-80"
        />
        <div class="grid gap-4">
          <div class="grid grid-flow-col gap-10 w-full items-center">
            <div class="w-full flex flex-col gap-4">
              <p class="flex items-center gap-2">
                <span class="font-bold"> Nombre: </span>
                <span class="font-mono">
                  {{ card.name }}
                </span>
              </p>

              <p class="flex items-center gap-2">
                <span class="font-bold"> Número: </span>
                <span class="font-mono">
                  {{
                    `${String(card.number).padStart(String(card.set?.total).length, '0')}/${card.set?.total}`
                  }}
                </span>
              </p>

              <p class="flex items-center gap-2">
                <span class="font-bold"> Set: </span>
                <span class="font-mono">
                  {{ card.set?.name }}
                </span>
              </p>

              <p class="flex items-center gap-2">
                <span class="font-bold"> Serie: </span>
                <span class="font-mono">
                  {{ card.set?.series }}
                </span>
              </p>
            </div>
            <div class="w-full flex flex-col gap-4">
              <p class="flex items-center gap-2">
                <span class="font-bold"> Categoría: </span>
                <Tag class="!bg-primary text-gray-100" :text="card.supertype" />
              </p>

              <div class="flex gap-2 items-center">
                <span class="font-bold"> {{ card.supertype }}:</span>
                <div class="flex gap-2">
                  <Tag :text="subtype" v-for="(subtype, id) in card.subtypes" :key="id" />
                </div>
              </div>

              <p class="flex items-center gap-2" v-if="card.rarity">
                <span class="font-bold"> Rareza: </span>
                <Tag class="!bg-green-600" :text="card.rarity" />
              </p>

              <div class="flex gap-2 items-center" v-if="card.types?.length">
                <span class="font-bold"> {{ card.types?.length > 1 ? 'Tipos' : 'Tipo' }}:</span>
                <div class="flex gap-2">
                  <Tag
                    :class="getTypeColor(type)"
                    :text="type"
                    v-for="(type, id) in card.types"
                    :key="id"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row-span-1 grid grid-flow-col gap-4 w-full items-center justify-center">
            <button
              type="button"
              class="bg-black text-gray-200 px-4 py-2 rounded-2xl flex items-center gap-2 max-w-28 justify-center max-h-10"
              :key="id"
              v-for="(market, id) in card.market"
              @click="openWeb(market.url)"
            >
              <svg-icon size="14" name="shop" />
              <span class="text-[0.8rem]">Comprar</span>
            </button>
          </div>
        </div>
      </section>
    </template>
  </card-component>
</template>
