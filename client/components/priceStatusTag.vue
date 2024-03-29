<template>
    <div
        class="flex flex-wrap w-full h-full rounded-lg text-[.75rem] font-bold p-1 leading-4 items-center"
        :class="isPriceDown ? 'bg-green-200 text-green-700' : 'bg-pink-100 text-red-600'"
    >
        <PriceDownIcon class="h-5 w-5 mr-1" v-if="isPriceDown" />
        <PriceUpIcon class="h-5 w-5 mr-1" v-else />
        {{ formatPrice(priceDifferent) }}
    </div>
</template>

<script setup lang="ts">
import PriceDownIcon from '~/assets/icons/priceDown.svg';
import PriceUpIcon from '~/assets/icons/priceUp.svg';
import { formatPrice } from '~/utils';

const props = defineProps({
    currentPrice: {
        type: Number,
        required: false,
        default: 0,
    },
    priceBeforeDiscount: {
        type: Number,
        required: false,
        default: 0,
    },
});

const priceDifferent = Math.abs(props.currentPrice - props.priceBeforeDiscount);
const isPriceDown = props.currentPrice < props.priceBeforeDiscount;
</script>

<style scoped></style>
