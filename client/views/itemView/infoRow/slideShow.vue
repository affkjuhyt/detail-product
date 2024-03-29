<template>
    <client-only>
        <a-image-preview-group>
            <a-carousel arrows dots-class="slick-dots slick-thumb">
                <template #customPaging="props">
                    <a>
                        <img :src="images[props.i]" alt="" />
                    </a>
                </template>

                <div v-for="item in images" :key="item" class="slideImg">
                    <a-image :src="item" alt="" />
                </div>
            </a-carousel>
        </a-image-preview-group>
    </client-only>
</template>

<script setup lang="ts">
defineProps<{
    images: string[];
}>();
</script>

<style scoped>
:global(.ant-image) {
    width: 100%;
    height: 100%;
    object-fit: contain;
}

:deep(.slick-dots) {
    position: relative;
    height: auto;
}

:deep(.slick-slide img) {
    display: block;
    margin: auto;
    max-width: 100%;
}

:deep(.slick-thumb) {
    bottom: 0;
}

:deep(.slick-thumb li) {
    width: 60px;
    height: 45px;
}

:deep(.slick-thumb li img) {
    width: 100%;
    height: 100%;
    display: block;
}
</style>
