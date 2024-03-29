<template>
    <h1 class="relative flex font-semibold text-base lg:text-lg text-gray-800 select-text mt-4 lg:mt-0">
        {{ itemDetailData.item.name }}
    </h1>

    <ReciveDiscountBtn class="my-2 lg:my-4" />

    <p class="flex flex-wrap items-center text-gray-600 mb-4">
        <span>Giá từ {{ getProviderName(itemDetailData.item.provider) }}</span>
        <img alt="Shopee" class="rounded-full ml-3 h-8" src="~/assets/images/shopee.jpg" />
    </p>

    <div class="flex lg:flex-col justify-between flex-col">
        <div class="h-full flex-grow flex justify-between lg:justify-start lg:flex-row lg:space-x-10 lg:items-center mb-3 flex-row">
            <div>
                <p class="text-2xl font-bold text-red-600">{{ formatPrice(itemDetailData.item.current_price) }}</p>
                <p class="text-sm line-through text-gray-600">{{ formatPrice(itemDetailData.item.price_before_discount) }}</p>
            </div>

            <div class="flex-shrink-0 h-7 mt-2 lg:mt-0">
                <PriceStatusTag :current-price="itemDetailData.item.current_price" :price-before-discount="itemDetailData.item.price_before_discount" />
            </div>

            <GoToShopBtn :link="itemDetailData.item.provider_url" />
        </div>

        <div class="flex flex-col-reverse lg:flex-col items-end lg:items-start">
            <div class="flex flex-col lg:flex-row items-end lg:items-center text-xs lg:text-sm">
                <div class="rating-star flex items-center space-x-1 md:w-auto mb-2 lg:mb-0 lg:mr-2">
                    <p class="text-yellow-400">{{ itemDetailData.item.rating_avg.toFixed(1) }}</p>

                    <StarRate :rate-avg="itemDetailData.item.rating_avg" />
                </div>

                <div class="flex flex-wrap space-x-2 justify-end lg:justify-start">
                    <div class="divideDesktopOnly">
                        <p>{{ itemDetailData.item.rating_count }} <span class="text-gray-500">đánh giá</span></p>
                    </div>

                    <div class="divideRegular pl-2 border-opacity-50">
                        <p>{{ itemDetailData.item.historical_sold }} <span class="text-gray-500">lượt bán</span></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import GoToShopBtn from '~/views/itemView/goToShopBtn.vue';
import PriceStatusTag from '~/components/priceStatusTag.vue';
import type { ItemDetail } from '~/types';
import { formatPrice } from '~/utils';

defineProps<{
    itemDetailData: ItemDetail;
}>();

function getProviderName(provider: string) {
    switch (provider) {
        case 'shopee':
            return 'Shopee';
        case 'tiki':
            return 'Tiki';
        case 'lazada':
            return 'Lazada';
        case 'sendo':
            return 'Sendo';
        default:
            return '';
    }
}
</script>

<style scoped>
@media (min-width: 768px) {
    .divideDesktopOnly {
        border-color: #d1d5db;
        border-left-width: 2px;
        padding-left: 0.75rem;
    }
}

.divideRegular {
    border-color: #d1d5db;
    border-left-width: 2px;
}
</style>
