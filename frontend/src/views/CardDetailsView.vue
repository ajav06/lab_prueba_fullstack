<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { onMounted, ref, type Ref } from 'vue';
import type { AxiosError } from 'axios';
import type { Card, ResponseAPIError } from '@/models';
import CardComponent from '@/components/CardComponent.vue';
import SvgIcon from '@/components/SvgIcon.vue';
import Tag from '@/components/Tag.vue';
import getCardById from '@/api/cardApis';
import { getTypeColor } from '@/helpers';

const route = useRoute();
const router = useRouter();
const card: Ref<Card> = ref({} as Card);
const loading: Ref<boolean> = ref(false);
const errorMessages: Ref<string> = ref('');

const fetchCard = async () => {
  try {
    loading.value = true;
    const response = await getCardById(String(route.params.cardId));
    card.value = response.results;
  } catch (err) {
    const error = err as AxiosError;
    errorMessages.value = (error.response?.data as ResponseAPIError)?.message || error.message;
    console.error(errorMessages.value);
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
    :title="card.name || errorMessages"
    :go-back="() => router.push({ name: 'CardsBySet', params: { setId: card.setId } })"
  >
    <template #content>
      <section
        v-if="card?.id"
        class="flex max-h-[26rem] justify-center gap-20 rounded-xl bg-gray-50 px-6 py-12"
      >
        <img
          :src="card.images?.find(({ type }) => type === 'small')?.url"
          :alt="card.name"
          class="max-h-80"
        />
        <div class="grid gap-4">
          <div class="grid w-full grid-flow-col items-center gap-10">
            <div class="flex w-full flex-col gap-4">
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
            <div class="flex w-full flex-col gap-4">
              <p class="flex items-center gap-2">
                <span class="font-bold"> Categoría: </span>
                <Tag class="!bg-primary text-gray-100" :text="card.supertype" />
              </p>

              <div class="flex items-center gap-2">
                <span class="font-bold"> {{ card.supertype }}:</span>
                <div class="flex gap-2">
                  <Tag :text="subtype" v-for="(subtype, id) in card.subtypes" :key="id" />
                </div>
              </div>

              <p class="flex items-center gap-2" v-if="card.rarity">
                <span class="font-bold"> Rareza: </span>
                <Tag class="!bg-green-600" :text="card.rarity" />
              </p>

              <div class="flex items-center gap-2" v-if="card.types?.length">
                <span class="font-bold"> {{ card.types?.length > 1 ? 'Tipos' : 'Tipo' }}:</span>
                <div class="flex gap-2">
                  <Tag
                    :color="getTypeColor(type)"
                    :text="type"
                    v-for="(type, id) in card.types"
                    :key="id"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="row-span-1 grid w-full grid-flow-col items-center justify-center gap-4">
            <button
              type="button"
              class="flex max-h-10 max-w-52 items-center justify-center gap-2 rounded-2xl bg-black px-4 py-2 text-gray-200"
              :key="id"
              v-for="(market, id) in card.market"
              @click="openWeb(market.url)"
            >
              <svg-icon size="14" name="shop" />
              <span class="text-[0.8rem]">Market: {{ market.market }}</span>
            </button>
          </div>
        </div>
      </section>
    </template>
  </card-component>
</template>
