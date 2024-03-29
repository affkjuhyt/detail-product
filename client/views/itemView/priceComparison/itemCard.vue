<template>
    <div class="flex md:items-center p-2 lg:p-4 rounded-xl cardShadow duration-100 ease-in">
        <div class="flex justify-start flex-auto">
            <div class="flex-shrink-0 cursor-pointer flex items-center">
                <div class="relative">
                    <img
                        alt="Hub chuyển đa năng 100W Baseus Metal Gleam Series Multifunctional Docking Station cho Macbook"
                        class="h-12 w-12 lg:h-20 lg:w-20"
                        src="https://cf.shopee.vn/file/2aff15e93b2101b5e1957b930c605871_tn"
                    />
                </div>
            </div>

            <div class="product-body flex justify-between items-center flex-auto ml-2">
                <div class="info-name overflow-hidden pr-2">
                    <div class="relative product-name break-words">
                        <a
                            href="#"
                            target="_self"
                            title="Hub chuyển đa năng 100W Baseus Metal Gleam Series Multifunctional Docking Station cho Macbook"
                            class="hover:text-primary-700 cursor-pointer"
                        >
                            <span data-v-52aa01fe="" class="leading-5 text-sm sm:text-base">
                                Hub chuyển đa năng 100W Baseus Metal Gleam Series Multifunctional Docking Station cho Macbook
                            </span>
                        </a>
                    </div>

                    <div class="flex sm:items-end flex-col sm:flex-row text-xs">
                        <div class="rating-star flex items-center space-x-1 md:w-auto mt-1 mr-2 md:mr-0 text-sm">
                            <p class="text-yellow-400">4.7</p>

                            <div class="flex flex-wrap items-center h-4 text-yellow-400">
                                <font-awesome-icon :icon="faStar" />
                                <font-awesome-icon :icon="faStar" />
                                <font-awesome-icon :icon="faStar" />
                                <font-awesome-icon :icon="faStar" />
                                <font-awesome-icon :icon="faStarHalfStroke" />
                            </div>
                        </div>

                        <div class="md:pl-3 md:mr-3"><span>11</span> <span class="text-gray-400">đánh giá</span></div>

                        <div class="divide-regular-l pl-3 border-opacity-50 hidden md:block">
                            <span>30</span> <span class="text-gray-400">lượt bán</span>
                        </div>
                    </div>
                </div>

                <div class="flex flex-col flex-wrap items-end space-y-1 cursor-pointer">
                    <div class="flex items-center min-w-max px-1">
                        <span class="text-red-600 font-medium"> 479.000&nbsp;₫ </span>
                    </div>

                    <div class="w-full">
                        <span
                            title="tăng 80.000&nbsp;₫"
                            class="flex flex-wrap bg-pink-100 text-red-600 w-full h-full rounded-lg text-[.75rem] p-1 items-center"
                        >
                            <PriceDownIcon class="h-5 w-auto mr-1" />
                            80.000&nbsp;₫
                        </span>
                    </div>
                </div>
            </div>
        </div>

        <div class="ml-2" style="max-width: 45%">
            <a class="btn px-2 py-2 md:px-5 md:py-3 text-sm border-blue-btn text-blue-btn border rounded hover:bg-blue-btn hover:text-white" href="#">
                <p class="inline-flex justify-center whitespace-nowrap items-center">
                    Đến nơi bán
                    <LongRightArrowIcon class="h-4 w-4 ml-1" />
                </p>
            </a>
        </div>
    </div>
</template>

<script setup lang="ts">
import { faStar, faStarHalfStroke } from '@fortawesome/free-solid-svg-icons';
import LongRightArrowIcon from 'assets/icons/longRightArrow.svg';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import PriceDownIcon from 'assets/icons/priceDown.svg';

defineComponent({
    name: 'PriceComparisonCard',
});
</script>

<style scoped>
.btn {
    transition-duration: 0.2s;
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

.cardShadow {
    box-shadow: rgba(157, 202, 196, 0.25) 0 7px 12px 0;
    @apply border border-transparent;
}

.cardShadow:hover {
    @apply border-gray-200;

    box-shadow:
        0 0 transparent,
        0 0 transparent,
        0 10px 15px -3px rgba(157, 202, 196, 0.5),
        0 4px 6px -2px rgba(0, 0, 0, 0.05);
}
</style>
