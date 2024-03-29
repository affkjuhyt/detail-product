<template>
    <client-only>
        <div class="flex flex-col overflow-hidden rounded-sm shadow hover:shadow-md cursor-pointer mb-1">
            <div class="h-full relative overflow-hidden">
                <img alt="" class="h-full w-full object-cover" src="https://cf.shopee.vn/file/be82e16ddc37dcf2657d02a30171a050_tn" />
            </div>

            <div class="h-max flex-shrink-0">
                <div class="h-full flex flex-col justify-around p-2 font-semibold text-gray-800 min-h-[128px]">
                    <div class="flex flex-row mb-0.5">
                        <div class="relative hover:text-primary-700 text-sm">
                            <p class="leading-5 line-clamp-2">Bộ hub mở rộng 8 in 1 baseus metal gleam lvm001</p>
                        </div>
                    </div>

                    <div class="mb-0.5 flex flex-wrap items-center justify-between">
                        <span class="text-sm text-green-700 px-2 py-1 bg-green-100 rounded-md">Có 1 nơi bán</span>
                    </div>

                    <div class="flex flex-wrap items-center justify-between">
                        <span class="text-red-500 text-base">Giá từ 530.000&nbsp;₫</span>
                    </div>

                    <div class="flex flex-wrap items-center">
                        <div class="flex items-center space-x-1 md:w-auto text-yellow-400">
                            <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                            <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                            <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                            <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                            <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                        </div>

                        <span class="text-gray-400 text-xs font-normal ml-1">(30)</span>
                    </div>
                </div>
            </div>
        </div>
    </client-only>
</template>

<script setup lang="ts">
import { faStar } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

defineComponent({
    name: 'ItemRelatedCard',
});
</script>

<style scoped></style>
