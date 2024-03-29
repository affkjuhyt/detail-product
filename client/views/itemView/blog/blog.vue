<template>
    <div class="w-full overflow-hidden mt-2">
        <div class="w-max lg:w-full flex flex-row flex-nowrap space-x-2 lg:space-x-4 mr-4 lg:mr-0">
            <div class="w-64 my-2 lg:my-0 lg:shadow-none lg:w-1/3" style="max-width: 450px" v-for="blog in blogs" :key="blog.id">
                <div class="flex flex-col overflow-hidden">
                    <div class="flex-shrink-0">
                        <a :href="blog.url" class="block mt-2">
                            <img
                                :src="blog.image_url"
                                :alt="blog.title"
                                class="w-full object-cover aspect-w7-h4"
                            />
                        </a>
                    </div>

                    <div class="flex-1 bg-white flex flex-col justify-between">
                        <div class="flex-1">
                            <a :href="blog.url" class="block my-2">
                                <p class="text-lg font-medium text-gray-900 line-clamp-2 h-14">
                                    {{  blog.title }}
                                </p>

                                <p class="mt-3 font-normal text-sm text-gray-500 line-clamp-3 h-16">
                                    {{ blog.description }}
                                </p>

                                <div class="bg-gray-200 h-10 flex justify-center items-center mt-5">
                                    <p class="uppercase">Đọc thêm</p>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="my-8 h-[1px] bg-gray-200"></div>
    </div>
</template>

<script setup lang="ts">
import type { BlogData } from '~/types';
defineComponent({
    name: 'BlogInItemView',
});

const props = defineProps({
    blogs: {
        type: Array as PropType<BlogData[]>,
        required: true,
    }
})

const blogs = ref(props.blogs);

</script>

<style scoped></style>
