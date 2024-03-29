<template>
    <div class="mt-6 lg:mt-0 max-w-sm mx-auto lg:ml-6 flex flex-wrap flex-col space-y-6 justify-center w-full lg:w-64 xl:w-80 h-full">
        <div class="rounded p-4 flex flex-col justify-between items-center border-primary-400 border">
            <ul class="space-y-2.5 leading-5 list-disc pl-5">
                <li>
                    Tổng thời gian biến động giá:
                    <span class="whitespace-nowrap">8 tháng</span>
                </li>

                <li>
                    Số lần thay đổi giá:
                    <span class="whitespace-nowrap">16 lần</span>
                </li>
            </ul>

            <div class="w-full mt-4 text-gray-600 text-[10px] text-right">
                <p>
                    Cung cấp bởi <a href="#"><span class="text-primary-400">Mua Thông Minh</span></a>
                </p>
            </div>
        </div>

        <div class="relative beeTip border border-primary-400 rounded p-4 pr-8 flex flex-col justify-between h-full">
            <img alt="icon-beecost" class="absolute -top-5 -right-6 h-28 w-28 shakeRotate" src="~/assets/images/mic.png" />

            <p class="mb-2 text-2xl font-semibold">Gợi ý dành cho bạn</p>

            <p class="mb-4">
                Tiện ích Mua Thông Minh giúp bạn xem tất cả các mức giá trong quá khứ của mọi sản phẩm (Shopee, Tiki, Lazada, Sendo).
                <strong>Tiết kiệm gấp đôi</strong>
            </p>

            <div class="flex flex-row justify-end items-center mb-4">
                <span class="text-gray-600 text-[10px] text-right w-full cursor-pointer"> Video hướng dẫn </span>

                <div class="fadeBtn ml-6 inline-flex bg-primary-500 text-white rounded items-center p-2 text-base cursor-pointer">
                    <span class="whitespace-nowrap cursor-pointer">Xem thêm chi tiết</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.beeTip {
    background: rgb(255, 251, 237);
}

.fadeBtn {
    background: linear-gradient(265.78deg, rgb(224, 121, 55) 0.54%, rgb(223, 163, 73) 99.62%);
}

.shakeRotate {
    animation: animation-rotate 4s ease-in-out 2s infinite;
    transform-origin: 50% 80%;
}

@keyframes animation-rotate {
    0% {
        transform: rotate(-5deg);
    }

    20% {
        transform: rotate(3deg);
    }

    40% {
        transform: rotate(-5deg);
    }

    55% {
        transform: rotate(3deg);
    }

    80% {
        transform: rotate(-5deg);
    }

    to {
        transform: rotate(0deg);
    }
}
</style>
