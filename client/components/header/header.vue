<template>
    <div class="bg-white py-3 md:py-4 md:border-b md:border-gray-300 md:border-opacity-50">
        <div class="flex items-center justify-between sm:justify-end container-v2 w-full overflow-hidden sm:overflow-visible">
            <div class="mr-6 flex-shrink-0">
                <a href="/">
                    <img src="assets/images/logoAppBeeCost.png" class="h-12 w-auto" alt="Logo" />
                </a>
            </div>

            <div class="relative text-gray-600 flex-grow max-w-xl mx-auto hidden sm:block">
                <div>
                    <input
                        placeholder="Dán link hoặc tìm sản phẩm"
                        tabindex="0"
                        class="placeholder-gray-400 w-full border border-gray-300 bg-white h-10 px-5 pr-12 rounded-full text-base focus:outline-none text-gray-800"
                    />

                    <div
                        class="absolute min-w-12 aspect-h1-w1 h-full inset-y-0 right-0 flex items-center justify-center cursor-pointer rounded-r-full text-primary-500 hover:text-blue-500"
                    >
                        <SearchIcon class="w-6 h-6" />
                    </div>
                </div>
            </div>

            <div class="flex flex-shrink-0 my-2 mx-4 lg:mr-0">
                <div class="flex flex-row items-center cursor-pointer" @click="toggleCategoryMenu">
                    <BarIcon />
                    <p class="ml-2 uppercase">Danh mục</p>
                </div>
            </div>

            <div class="relative ml-4">
                <a href="/blog" class="hover:text-primary-700 uppercase">Blog</a>
            </div>
        </div>
    </div>

    <CategoryComponent v-if="isCategoryMenuOpen" :toggle="toggleCategoryMenu" :categories="categoriesData" />
</template>

<script setup lang="ts">
import SearchIcon from '~/assets/icons/searchIcon.svg';
import BarIcon from '~/assets/icons/menuBar.svg';
import CategoryComponent from '~/components/header/category.vue';

defineComponent({
    name: 'HeaderComponent',
});

const isCategoryMenuOpen = ref(false);

const toggleCategoryMenu = () => {
    isCategoryMenuOpen.value = !isCategoryMenuOpen.value;
};

watch(isCategoryMenuOpen, (value) => {
    if (value) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
});

onUnmounted(() => {
    document.body.style.overflow = 'auto';
});

const categoriesData = ref([]);

const { error, data } = await useCustomFetch(`/category/list`);

if (error.value) {
    console.error(error.value);
}

if (data.value) {
    categoriesData.value = data.value.data;
}

console.log('categoriesData: ', categoriesData);
</script>
