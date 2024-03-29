<template>
    <div class="mt-2 mx-6 lg:mx-auto">
        <div class="text-lg font-medium pb-1 mb-4">Gợi ý hôm nay</div>

        <div class="grid-responsive-custom relative z-0">
            <ItemCard v-for="i in 10" :key="i" />
        </div>
    </div>
</template>

<script setup lang="ts">
import ItemCard from '~/components/itemCard.vue';
</script>

<style scoped></style>
