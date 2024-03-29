<template>
    <div class="flex flex-wrap space-x-4 items-center">
        <a class="bg-primary-500 w-full px-3 md:px-6 py-3 text-sm rounded text-white" :href="link" target="_blank">
            <p class="btn inline-flex text-center whitespace-nowrap">
                Đến nơi bán
                <LongRightArrow class="ml-1 h-5" />
            </p>
        </a>
    </div>
</template>

<script setup lang="ts">
import LongRightArrow from 'assets/icons/longRightArrow.svg';

defineProps<{
    link: string;
}>();
</script>

<style scoped>
.btn:hover {
    animation: slide-bt-custom 0.15s ease-in-out;
    font-weight: 700;
}

@keyframes slide-bt-custom {
    0% {
        opacity: 0;
        transform: translateY(-8px);
    }

    90% {
        opacity: 1;
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
