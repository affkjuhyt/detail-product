<template>
    <div class="flex flex-wrap items-center h-4 text-yellow-400">
        <font-awesome-icon :icon="faStar" class="h-3 lg:h-4" v-for="i in wholeStars" :key="i" />
        <font-awesome-icon :icon="faStarHalfStroke" class="h-3 lg:h-4" v-if="halfStar" />
    </div>
</template>

<script setup lang="ts">
import { faStar, faStarHalfStroke } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const props = defineProps<{
    rateAvg: number;
}>();

const rateAvg = ref(props.rateAvg);

const wholeStars = computed(() => Math.floor(rateAvg.value));
const halfStar = computed(() => rateAvg.value % 1 >= 0.5);
</script>

<style scoped></style>
