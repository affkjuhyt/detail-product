<template>
    <div id="priceHistory" class="flex lg:justify-between justify-start items-start my-2">
        <div class="text-lg font-medium pb-1 mb-4">Lịch sử giá</div>

        <ReciveDiscountBtn />
    </div>

    <div class="flex flex-col lg:flex-row">
        <LeftCol :item-detail-data="itemDetailData" />
        <RightCol />
    </div>
</template>

<script setup lang="ts">
import LeftCol from '~/views/itemView/priceHistory/leftCol.vue';
import RightCol from '~/views/itemView/priceHistory/rightCol.vue';
import type { ItemDetail } from '~/types';

defineProps<{
    itemDetailData: ItemDetail;
}>();
</script>

<style scoped></style>
