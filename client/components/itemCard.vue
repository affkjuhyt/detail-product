<template>
    <a href="#" class="text-xs" style="z-index: 14">
        <div
            class="relative shadow cursor-pointer duration-150 ease-in justify-between h-full w-full hover:border-primary-500 hover:border -translate-y-0.5"
        >
            <div class="w-full relative overflow-hidden flex-shrink-0 hover:scale-95 duration-75 ease-in" style="max-height: 66.67%">
                <img
                    alt="Lazada"
                    class="absolute top-2 left-2 w-8 h-8 opacity-80 rounded-full"
                    src="https://lh3.googleusercontent.com/pw/AM-JKLXdejwgK7qJVJ6zZNxxFv4IIzn07zmFU32lBG94DuS4jPUsRqI__7szNL1jD1DNVrexFON7ZTiqqZPV3pDuzmv9YZukejnqbJvLJ1t-1Ym1vqUCX6fBL6V3Gv5qOlysOXtfNaIW2VotW1_yNB9GaIja"
                />

                <img
                    alt="Mặt Nạ Đất Sét Kiềm Dầu Ngừa Mụn Se Khít Lỗ Chân Lông Cho Nam EAST MOON Làm Sạch Mụn Kiểm Soát Dầu Loại Bỏ Mụn Đầu Đen Làm Mát Da Dưỡng Ẩm Sáng Da"
                    class="w-full object-cover overflow-hidden aspect-h1-w1"
                    src="https://vn-live-01.slatic.net/p/8a21b9743c59188157fe20c7419bb2ea.png"
                />
            </div>

            <div class="h-max flex-shrink-0">
                <div class="h-full flex flex-col justify-around p-2 text-gray-800" style="min-height: 128px">
                    <div class="product-name-wrap flex flex-row">
                        <div class="relative hover:text-primary-700 text-xs sm:text-sm lg:text-base">
                            <p class="leading-5 line-clamp-2 break-words">
                                Mặt nạ đất sét kiềm dầu ngừa mụn se khít lỗ chân lông cho nam east moon làm sạch mụn kiểm soát dầu loại bỏ mụn đầu đen
                                làm mát da dưỡng ẩm sáng da
                            </p>
                        </div>
                    </div>

                    <div class="mt-0.5 flex flex-wrap items-center justify-between font-semibold">
                        <span class="text-red-500 text-sm sm:text-base">130.000&nbsp;₫</span>

                        <div>
                            <PriceStatusTag />
                        </div>
                    </div>

                    <div class="flex flex-wrap items-center">
                        <div class="rating-star flex items-center space-x-1 md:w-auto">
                            <div class="flex flex-wrap items-center h-4 text-yellow-400">
                                <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                                <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                                <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                                <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                                <FontAwesomeIcon :icon="faStar" class="w-3 h-3" />
                            </div>
                        </div>

                        <span class="text-gray-400 text-xs font-normal ml-1">(19)</span>
                    </div>
                </div>
            </div>
        </div>
    </a>
</template>

<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faStar } from '@fortawesome/free-solid-svg-icons';

defineComponent({
    name: 'ItemCard',
});
</script>

<style scoped></style>
