<template>
    <div class="mt-2 mx-6 lg:mx-auto">
        <div class="text-lg font-medium pb-1 mb-4">Gợi ý dành cho bạn</div>

        <div>
            <client-only>
                <swiper
                    :modules="[SwiperNavigation]"
                    :slides-per-view="4"
                    :space-between="12"
                    :navigation="{
                        nextEl: '.swiper-button-next',
                        prevEl: '.swiper-button-prev',
                    }"
                >
                    <swiper-slide v-for="i in 10" :key="i">
                        <ItemCard />
                    </swiper-slide>

                    <div class="swiper-button-prev swiper-button-arr"></div>
                    <div class="swiper-button-next swiper-button-arr"></div>
                </swiper>
            </client-only>
        </div>

        <div class="my-8 h-[1px] bg-gray-200"></div>
    </div>
</template>

<script setup lang="ts">
import ItemCard from '~/components/itemCard.vue';
</script>

<style scoped></style>
