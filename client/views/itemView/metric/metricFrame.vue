<template>
    <div class="mt-16 hidden lg:block frame mb-16">
        <div class="mt-2 p-0">
            <iframe src="https://beecostvnwd.metric.vn/iframe/market_widget_chart" width="100%" height="950px" />
        </div>
    </div>

    <div class="bg-white relative mt-12 mb-24">
        <div class="mx-auto py-4">
            <div class="rounded-lg overflow-hidden lg:grid lg:grid-cols-2 lg:gap-4" style="background: rgba(35, 104, 212, 0.2)">
                <div class="pt-10 pb-12 px-6 sm:pt-16 sm:px-16 lg:px-20 lg:py-16 lg:pr-0 xl:py-20 xl:px-20">
                    <div class="lg:self-center text-black">
                        <div class="text-xl font-bold sm:text-2xl">
                            <span class="block">Bạn muốn xem tất cả lịch sử giá của <span class="text-primary-500">Shopee</span>?!</span>
                        </div>

                        <p class="mt-4 text-lg leading-6">Cài đặt ngay Mua Thông Minh Extension phát hiện sale ảo, sale xịn nhé!</p>

                        <p class="mt-4 text-lg leading-6">Chỉ tốn 3 giây mà siêu tiện, siêu hời!</p>
                        <div
                            class="mt-8 bg-primary-500 border border-transparent rounded-md shadow px-5 py-3 inline-flex items-center text-base font-medium text-white hover:bg-primary-400 cursor-pointer"
                        >
                            <a target="_blank" href="https://chromewebstore.google.com/detail/mua-th%C3%B4ng-minh/hfgkoaengklibhfagaababcngpehggmm?utm_source&pli=1">
                                Thêm Mua Thông Minh vào Chrome/Cốc Cốc
                            </a>
                        </div>
                    </div>
                </div>

                <div class="absolute" style="top: -84px; right: 120px">
                    <img
                        alt="BeeCost"
                        class="transform translate-x-6 translate-y-6 rounded-md object-cover object-left-top sm:translate-x-16 lg:translate-y-20"
                        src="https://lh3.googleusercontent.com/KFm2SMk264Yy9KOyJLDzeQ4vveaRN5SbI5sWE5kmZWDiqOAubwyUrThDIpd1__r0mRrNjOOIMJxuEqgGZ_ea1yFOf0_MMZOPgcj5rYTy3W1X29ebwU7EXHI0wvV4PH9xucvfneEAdw=w498-h430-no"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.frame {
    border: 1px solid #cbe0ff;
    box-shadow: 0 8px 12px rgba(203, 223, 255, 0.25);
}
</style>
