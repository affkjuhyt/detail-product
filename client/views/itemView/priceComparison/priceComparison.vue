<template>
    <div class="mr-4 lg:mr-0 mt-2">
        <div class="text-lg font-medium mb-4 pb-1">So sánh giá</div>

        <div class="space-y-4">
            <div class="text-gray-600">
                Tìm thấy <span class="font-medium text-gray-700">13</span> nơi bán khác, giá từ
                <span class="font-medium text-gray-700"> 450.000&nbsp;₫ - 499.000&nbsp;₫</span>
            </div>

            <div>
                <div class="mb-2">
                    <img alt="platform" class="w-auto h-10" src="~/assets/images/shopee-logo-text.png" />
                </div>

                <div class="space-y-4">
                    <PriceComparisonCard />
                    <PriceComparisonCard />
                    <PriceComparisonCard />
                    <PriceComparisonCard />
                </div>
            </div>

            <div>
                <div class="mb-2 mt-6">
                    <img alt="lazada" class="w-auto h-8" src="~/assets/images/lazada-logo-text.png" />
                </div>

                <div class="space-y-4">
                    <PriceComparisonCard />
                    <PriceComparisonCard />
                    <PriceComparisonCard />
                    <PriceComparisonCard />
                </div>
            </div>

            <div class="flex justify-center">
                <div
                    class="inline-flex px-2 py-2 md:px-5 md:py-3 border-transparent hover:bg-gray-50 hover:text-black text-sm cursor-pointer"
                    style="box-shadow: rgba(207, 207, 207, 0.25) 0 4px 4px 0"
                >
                    <p class="inline-flex items-center justify-center">
                        Xem thêm 7 nơi bán khác
                        <font-awesome-icon :icon="faChevronDown" class="ml-2 h-4" />
                    </p>
                </div>
            </div>
        </div>

        <div class="my-4 bg-gray-200 w-full h-[1px]"></div>
    </div>
</template>

<script setup lang="ts">
import PriceComparisonCard from '~/views/itemView/priceComparison/itemCard.vue';
import { faChevronDown } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
</script>

<style scoped></style>
