<script setup lang="ts">
import { computed, ref, watch, type ComputedRef, type Ref } from 'vue';
import SvgIcon from './SvgIcon.vue';

interface Props<T> {
  headers: { text: string; field: string }[];
  items: T;
  itemsPerPage: number;
  searchQuery: string;
}

const props: Props<any> = defineProps<Props<any>>();

const currentPage: Ref<number> = ref(1);
const itemsPerPage: Ref<number> = ref(props.itemsPerPage);

const filteredItems: ComputedRef<typeof props.items> = computed(() => {
  if (!props.searchQuery) {
    return props.items;
  }

  const query = props.searchQuery.toLowerCase();
  return props.items.filter((item: { [x: string]: any }) => {
    return props.headers.some((header) => {
      if (['actions', 'Url'].includes(header.field)) {
        return false;
      }
      if (['subtypes', 'types'].includes(header.field)) {
        return item[header.field].some((value: string) => value.toLowerCase().includes(query));
      }
      let text = String(item[header.field] ?? '');
      if (header.field.toLowerCase().includes('date')) {
        [text] = text.split(' ');
      }
      text = text.toLowerCase();
      return text.includes(query);
    });
  });
});
const paginatedItems: ComputedRef<typeof props.items> = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return filteredItems.value.slice(start, end);
});
const totalPages: ComputedRef<number> = computed(() =>
  Math.ceil(filteredItems.value.length / itemsPerPage.value),
);
const visiblePages: ComputedRef<(number | string)[]> = computed(() => {
  if (totalPages.value <= 3)
    return Array.from({ length: totalPages.value }, (_, index) => index + 1);

  const pages: (number | string)[] = [1];

  if (currentPage.value > 2) {
    pages.push(currentPage.value - 1);
  }

  if (currentPage.value !== 1 && currentPage.value !== totalPages.value) {
    pages.push(currentPage.value);
  }

  if (currentPage.value < totalPages.value - 1) {
    pages.push(currentPage.value + 1);
  }

  pages.push(totalPages.value);
  return pages;
});

const goToPage = (page: number) => {
  if (page > 0 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

watch(
  () => props.searchQuery,
  () => {
    goToPage(1);
  },
);
</script>

<template>
  <main class="max-w-full overflow-x-auto">
    <table class="min-w-full divide-y divide-gray-200">
      <thead>
        <tr>
          <th
            v-for="(header, id) in props.headers"
            :key="id"
            class="bg-gray-50 px-6 py-3 text-left text-xs font-medium uppercase leading-4 tracking-wider text-gray-500 first:rounded-tl-xl last:rounded-tr-xl"
          >
            {{ header.text }}
          </th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-200 rounded-bl-xl bg-white">
        <tr v-for="(item, id) in paginatedItems" :key="id">
          <td
            class="whitespace-no-wrap px-6 py-4"
            :class="{ 'first:rounded-bl-xl last:rounded-br-xl': id === paginatedItems.length - 1 }"
            v-for="(header, _id) in props.headers"
            :key="_id"
          >
            <slot :name="header.field" :value="item" :index="id">
              {{ item[header.field] }}
            </slot>
          </td>
        </tr>
      </tbody>
    </table>
    <div
      class="mx-auto mt-4 flex max-w-full justify-center"
      v-if="props.items.length > 0 && filteredItems.length > props.itemsPerPage"
    >
      <button
        type="button"
        @click="goToPage(currentPage - 1)"
        class="px-[0.844rem] py-[0.313rem] text-gray-500"
        :disabled="currentPage === 1"
      >
        <svg-icon name="chevron-left" size="12" />
      </button>

      <button
        v-for="page in visiblePages"
        :key="page"
        type="button"
        @click="goToPage(parseInt(String(page)))"
        class="rounded-md px-[0.844rem] py-[0.313rem] text-xs"
        :class="{
          'bg-primary text-secondary': page === currentPage,
          'text-gray-900': [currentPage - 1, currentPage + 1].includes(parseInt(String(page))),
          'text-gray-600':
            ![currentPage - 1, currentPage].includes(parseInt(String(page))) &&
            page !== currentPage,
        }"
      >
        {{ page }}
      </button>

      <button
        type="button"
        @click="goToPage(currentPage + 1)"
        class="px-[0.844rem] py-[0.313rem] text-gray-500"
        :disabled="currentPage === totalPages"
      >
        <svg-icon name="chevron-right" size="12" />
      </button>
    </div>
  </main>
</template>
