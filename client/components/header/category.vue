<template>
    <div class="fixed top-0 left-0 z-40 w-full h-screen flex items-start justify-start bg-white overflow-hidden flex-row">
        <div class="h-screen border-r border-gray-200 hidden sm:flex w-72 xl:w-96">
            <ul class="h-screen w-full flex flex-col flex-shrink-0 items-start justify-start slide-bt overflow-y-auto hide-scrollbar">
                <li
                    class="menuItem"
                    v-for="category in categories"
                    :key="category.id"
                    :class="category?.id === currentParentCategory?.id ? 'active' : ''"
                    @click="changeCurrentParentCategory(category)"
                >
                    <div class="h-10 w-10 overflow-hidden rounded-full">
                        <img alt="" class="h-10 w-10" src="~/assets/images/shopee.jpg" />
                    </div>

                    <a rel="nofollow" href="#" class="ml-2">{{ category.name }}</a>
                </li>
            </ul>
        </div>

        <div class="relative h-screen w-full">
            <div class="fixed w-full pl-4 sm:pt-10 sm:pl-10 top-0 pt-8">
                <font-awesome-icon
                    :icon="faXmark"
                    class="fixed top-2 right-2 h-6 w-6 p-2 cursor-pointer rounded-full hover:bg-gray-200"
                    @click="toggle"
                />

                <p class="text-2xl mb-6">{{ currentParentCategory?.name }}</p>

                <ul
                    class="h-full w-full sm:w-4/5 2xl:w-3/5 flex flex-col sm:grid grid-cols-1 md:grid-cols-2 2xl:grid-cols-3 gap-2 sm:gap-3 2xl:gap-4"
                    v-if="currentParentCategory?.childs"
                >
                    <li class="flex-shrink-0 hover:text-primary-500" v-for="item in currentParentCategory?.childs" :key="item.id">
                        <a rel="nofollow" href="#">{{ item.name }}</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faXmark } from '@fortawesome/free-solid-svg-icons';
import type { CategoryData } from '~/types';
import type { PropType } from 'vue';

defineComponent({
    name: 'CategoryComponent',
});

const props = defineProps({
    toggle: Function,
    categories: {
        type: Array as PropType<CategoryData[]>,
        required: true,
    },
});

console.log('categories: ', props.categories)

const currentParentCategory = ref(props.categories[0]);

function changeCurrentParentCategory(category: CategoryData) {
    currentParentCategory.value = category;
}

console.log('currentParentCategory: ', currentParentCategory);
</script>

<style scoped>
.hide-scrollbar {
    scrollbar-width: none;
    -ms-overflow-style: none;
}

.menuItem {
    @apply w-full flex flex-row items-center justify-start px-4 py-2.5 leading-5 cursor-pointer hover:bg-gray-100;
}

.active {
    @apply bg-gray-200 font-semibold;
}
</style>
