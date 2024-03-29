<template>
    <div id="itemDescription" class="mx-6 lg:mx-auto mt-2">
        <div class="text-lg font-medium pb-1 mb-4">Mô tả sản phẩm</div>

        <blockquote>
            <div class="sortContent" :class="isExpanded ? '' : 'hideContent'">{{ description }}</div>

            <p class="text-primary-500 text-lg underline cursor-pointer mt-5" @click="toggleExpand">
                {{ isExpanded ? 'Thu nhỏ' : 'Xem thêm' }}
            </p>
        </blockquote>
    </div>

    <div class="h-[1px] bg-gray-200 my-8"></div>
</template>

<script setup lang="ts">
const isExpanded = ref(false);

function toggleExpand() {
    isExpanded.value = !isExpanded.value;
}

defineProps<{
    description: string;
}>();
</script>

<style scoped>
.hideContent:after {
    background: linear-gradient(0deg, hsla(0, 0%, 100%, 0.65), hsla(0, 0%, 100%, 0));
    bottom: 0;
    content: '';
    height: 80px;
    left: 0;
    pointer-events: none;
    position: absolute;
    right: 0;
}

.sortContent {
    position: relative;
    word-wrap: break-word;
    line-height: 2rem;
    transition-duration: 0.5s;
    transition-property: max-height;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    white-space: pre-wrap;
}

.hideContent {
    max-height: 24rem;
    overflow: hidden;
}
</style>
