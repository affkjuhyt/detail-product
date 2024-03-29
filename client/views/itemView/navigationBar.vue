<template>
    <div class="h-16 lg:shadow-none shadow-custom w-full bg-white">
        <ul class="inpage-navigation flex flex-row w-full sm:pt-3">
            <li class="sectionItem active">
                <PriceCompareIcon class="hidden sm:block h-6 w-6 mb-1" />
                <span data-v-1fe37343="">So sánh giá</span>
            </li>

            <a href="#priceHistory">
                <li class="sectionItem">
                    <PriceHistoryIcon class="hidden sm:block h-6 w-6 mb-1" />
                    <span data-v-1fe37343="">Lịch sử giá</span>
                </li>
            </a>

            <a href="#itemDescription">
                <li class="sectionItem">
                    <ItemDescriptionIcon class="hidden sm:block h-6 w-6 mb-1" />
                    <span data-v-1fe37343="">Mô tả sản phẩm</span>
                </li>
            </a>

            <a href="#itemReview">
                <li class="sectionItem">
                    <itemReviewIcon class="hidden sm:block h-6 w-6 mb-1" />
                    <span>Đánh giá từ người mua</span>
                </li>
            </a>
        </ul>
    </div>
</template>

<script setup lang="ts">
import PriceCompareIcon from '~/assets/icons/priceCompare.svg';
import PriceHistoryIcon from '~/assets/icons/priceHistory.svg';
import ItemDescriptionIcon from '~/assets/icons/itemDescription.svg';
import itemReviewIcon from '~/assets/icons/itemReview.svg';
</script>

<style scoped>
.sectionItem {
    @apply flex flex-row space-x-2 font-medium mr-1 px-3 lg:pb-3 lg:border-b-2 text-gray-500 cursor-pointer;
}

.sectionItem:hover {
    @apply active;
    transition-duration: 0.3s;
    transition-property:
        background-color,
        border-color,
        color,
        fill,
        stroke,
        opacity,
        box-shadow,
        transform,
        filter,
        backdrop-filter,
        -webkit-backdrop-filter;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

.active {
    @apply text-gray-700 border-primary-600;
}
</style>
