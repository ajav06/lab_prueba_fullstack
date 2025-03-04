<script setup lang="ts">
import { computed, ref, type ComputedRef, type Ref } from 'vue';
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
      if (['actions', 'id', 'enabled'].includes(header.field)) {
        return false;
      }
      let text = String(item[header.field] ?? '');
      if (header.field.toLowerCase().includes('date')) {
        [text] = text.split('T');
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
  Math.ceil(props.items.length / itemsPerPage.value),
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
</script>

<template>
  <main class="max-w-full overflow-x-auto">
    <table class="min-w-full divide-y divide-gray-200">
      <thead>
        <tr>
          <th
            v-for="(header, id) in props.headers"
            :key="id"
            class="first:rounded-tl-xl last:rounded-tr-xl px-6 py-3 bg-gray-50 text-left text-xs leading-4 font-medium text-gray-500 uppercase tracking-wider"
          >
            {{ header.text }}
          </th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200 rounded-bl-xl">
        <tr v-for="(item, id) in paginatedItems" :key="id">
          <td
            class="px-6 py-4 whitespace-no-wrap"
            :class="{ 'last:rounded-br-xl first:rounded-bl-xl': id === paginatedItems.length - 1 }"
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
      class="mt-4 flex max-w-full justify-center mx-auto"
      v-if="props.items.length > 0 && props.items.length > props.itemsPerPage"
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
