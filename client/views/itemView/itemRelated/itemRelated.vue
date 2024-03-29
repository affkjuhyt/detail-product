<template>
    <div class="mt-8">
        <div class="mt-2 mx-6 lg:mx-auto">
            <div class="text-lg font-medium pb-1 mb-4">Sản phẩm liên quan</div>

            <div>
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
                        <ItemRelatedCard />
                    </swiper-slide>

                    <div class="swiper-button-prev swiper-button-arr"></div>
                    <div class="swiper-button-next swiper-button-arr"></div>
                </swiper>
            </div>
        </div>
    </div>

    <div class="my-8 h-[1px] bg-gray-200"></div>
</template>

<script setup lang="ts">
import ItemRelatedCard from '~/views/itemView/itemRelated/itemCard.vue';
</script>

<style scoped></style>
