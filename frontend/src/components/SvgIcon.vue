<script setup lang="ts">
import { type Ref, ref, onMounted } from 'vue';

interface Props {
  name: string;
  svgClass?: string;
  size?: string;
}

const props = defineProps<Props>();

const svgContent: Ref<string> = ref('');

const loadSVG = async () => {
  try {
    const svgModule = await import(`@/assets/icons/${props.name}.svg?raw`);
    let svgText = svgModule.default;

    if (props.size) {
      svgText = svgText.replace(/width="[^"]*"/, `width="${props.size}"`);
      svgText = svgText.replace(/height="[^"]*"/, `height="${props.size}"`);
    }
    svgContent.value = svgText;
  } catch (error) {
    console.error('Error fetching SVG:', error);
  }
};

onMounted(loadSVG);
</script>

<template>
  <i v-if="svgContent" v-html="svgContent" :class="svgClass" />
</template>
