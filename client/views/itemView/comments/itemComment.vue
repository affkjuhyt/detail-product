<template>
    <div class="border-b border-gray-200 text-gray-500 space-y-2 text-sm pb-4">
        <div class="w-full flex flex-row">
            <img alt="annatrinh2001" class="h-10 w-10 mr-4 rounded-full" src="https://cf.shopee.vn/file/3958d01eeaaf632ee0bb594590303a22_tn" />

            <div class="flex flex-wrap flex-col items-start text-xs space-y-1">
                <div class="flex flex-wrap space-x-2">
                    <p>annatrinh2001</p>

                    <p class="flex items-center text-green-500 font-medium">
                        <FontAwesomeIcon :icon="faCheckCircle" class="h-3 mr-1" />
                        <span> Đã mua tại Shopee </span>
                    </p>
                </div>

                <div class="rating-star flex items-center space-x-1 md:w-auto w-full">
                    <div class="flex flex-wrap items-center h-4 text-yellow-400">
                        <FontAwesomeIcon :icon="faStar" />
                        <FontAwesomeIcon :icon="faStar" />
                        <FontAwesomeIcon :icon="faStar" />
                        <FontAwesomeIcon :icon="faStar" />
                        <FontAwesomeIcon :icon="faStar" />
                    </div>
                </div>
            </div>
        </div>

        <div class="overflow-hidden text-gray-600 max-width-text">
            Sp tốt Mua lúc 8g tối 9g nhận được luôn Shop dịch vụ tốt Mình dùng type c qua monitor 4k đường hdmi i
        </div>

        <a-image-preview-group>
            <div class="flex flex-row flex-wrap space-x-2">
                <a-image :width="100" :height="100" class="object-cover" src="https://cf.shopee.vn/file/77bd432952a494ecf86d3b7992f2e515_tn" />

                <a-image :width="100" :height="100" class="object-cover" src="https://cf.shopee.vn/file/1fa4aba5bdbd00aae40a1ffa5e6b8bc5_tn" />

                <a-image :width="100" :height="100" class="object-cover" src="https://cf.shopee.vn/file/fd9f55f1aa284cf8f0ad6660a39fa9f8_tn" />

                <a-image :width="100" :height="100" class="object-cover" src="https://cf.shopee.vn/file/bc4cf053e366300af40b15b4212c2a33_tn" />

                <a-image
                    :width="100"
                    :height="100"
                    class="object-cover"
                    src="https://play-tx.vod.shopee.com/c3/98934353/103/AmM1gYMAEE=mRvMhSgEGLsxH.jpg"
                />
            </div>
        </a-image-preview-group>

        <p class="text-xs">2 năm trước</p>
    </div>
</template>

<script setup lang="ts">
import { faCheckCircle } from '@fortawesome/free-regular-svg-icons';
import { faStar } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
</script>

<style scoped>
.max-width-text {
    max-width: 900px !important;
}
</style>
