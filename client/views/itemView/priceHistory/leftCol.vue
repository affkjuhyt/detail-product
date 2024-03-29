<template>
    <div class="flex-grow border-primary-400 border rounded p-4 min-h-max">
        <div class="w-full flex justify-between">
            <div class="flex flex-row justify-start">
                <span class="text-lg font-medium text-primary-400">Biến động giá</span>
                <img src="~/assets/images/logo-transparent.png" alt="icon beecost" class="w-6 h-6" />
            </div>

            <div>
                <div class="w-full flex justify-end items-center space-x-2 mb-2">
                    <span class="text-sm">Giá hiện tại:</span>
                    <span class="text-lg font-medium">{{ formatPrice(itemDetailData.item.current_price) }}</span>
                </div>

                <div class="flex flex-row space-x-4 mb-2 text-sm">
                    <div class="min-price display-row2">
                        Từ
                        <span class="mx-2 px-3 py-1 bg-gray-200">
                            {{ firstPriceDate }}
                        </span>
                    </div>

                    <div class="max-price display-row2">
                        Đến
                        <span class="ml-2 px-3 py-1 bg-gray-200">
                            {{ lastPriceDate }}
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <div>
            <div class="flex flex-row space-x-4 mb-2 ml-2 text-sm">
                <div>
                    Cao nhất:
                    <span class="text-red-400">{{ formatPrice(maxPrice) }}</span>
                </div>

                <div>
                    Thấp nhất:
                    <span class="text-green-600">{{ formatPrice(minPrice) }}</span>
                </div>
            </div>

            <PriceChart v-if="isLoadingChart" :price-history-data="priceHistoryData" />

            <div class="flex justify-center mt-10" v-else>
                <a-spin size="large" />
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import PriceChart from '~/views/itemView/priceHistory/priceChart.vue';
import type { ItemDetail, PriceHistory } from '~/types';
import dayjs from 'dayjs';

const props = defineProps<{
    itemDetailData: ItemDetail;
}>();

const isLoadingChart = ref(false);

const { data, error } = await useCustomFetch(`/item/${props.itemDetailData.item.id}/price-history`);

if (error.value) {
    isLoadingChart.value = false;
}

if (data.value) {
    isLoadingChart.value = true;
}

const priceHistoryData: PriceHistory[] = data.value?.data;

console.log('priceHistoryData: ', priceHistoryData);

const firstPriceDate = priceHistoryData.length > 0 ? dayjs(priceHistoryData[0].created_at).format('DD - MM - YYYY') : 'Updating';
const lastPriceDate =
    priceHistoryData.length > 0 ? dayjs(priceHistoryData[priceHistoryData.length - 1].created_at).format('DD - MM - YYYY') : 'Updating';

const maxPrice = priceHistoryData.reduce((prev, current) => (prev > current.price ? prev : current.price), 0);
const minPrice = priceHistoryData.reduce((prev, current) => (prev < current.price ? prev : current.price), maxPrice);
</script>

<style scoped></style>
