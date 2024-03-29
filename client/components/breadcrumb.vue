<template>
    <div class="container-v2 mb-4 lg:mb-0">
        <nav class="flex px-4 sm:px-0 ml-4 lg:ml-0 p-0">
            <ol class="flex items-center lg:space-x-4 md:space-x-2 overflow-hidden overflow-x-auto hide-scrollbar">
                <li class="flex items-center lg:py-2">
                    <a href="/" class="text-gray-600 hover:text-primary-700">
                        <HomeIcon class="flex-shrink-0 h-5 w-5" />
                        <span itemprop="name" class="sr-only">Homepage</span>
                    </a>
                </li>

                <li class="flex items-center lg:py-2">
                    <RightIcon class="flex-shrink-0 h-5 w-5 text-gray-600 mr-2 md:mr-4" />

                    <a href="#" class="text-gray-600 hover:text-primary-700 text-sm font-medium whitespace-nowrap" itemprop="item">
                        Máy tính & Laptop
                    </a>
                </li>

                <li class="flex items-center lg:py-2">
                    <RightIcon class="flex-shrink-0 h-5 w-5 text-gray-600 mr-2 md:mr-4" />

                    <a href="#" class="text-gray-600 hover:text-primary-700 text-sm font-medium whitespace-nowrap" itemprop="item">
                        Phụ Kiện Máy Tính
                    </a>
                </li>

                <li class="flex items-center lg:py-2">
                    <RightIcon class="flex-shrink-0 h-5 w-5 text-gray-600 mr-2 md:mr-4" />

                    <a href="#" class="text-gray-600 hover:text-primary-700 text-sm font-medium whitespace-nowrap" itemprop="item">
                        Bộ chia cổng USB & Đọc thẻ nhớ
                    </a>
                </li>
            </ol>
        </nav>
    </div>
</template>

<script setup lang="ts">
import HomeIcon from '~/assets/icons/home.svg';
import RightIcon from '~/assets/icons/rightArrow.svg';

defineComponent({
    name: 'BreadcrumbComponent',
});
</script>
