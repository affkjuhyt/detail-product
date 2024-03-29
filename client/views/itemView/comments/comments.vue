<template>
    <div id="itemReview" class="mx-6 lg:mx-auto mt-2">
        <div class="text-lg font-medium mb-4 pb-1">Đánh giá từ người mua</div>

        <div class="flex flex-col space-y-4 border-b-1">
            <ItemComment />
            <ItemComment />
            <ItemComment />
        </div>
    </div>
</template>

<script setup lang="ts">
import ItemComment from '~/views/itemView/comments/itemComment.vue';

defineComponent({
    name: 'ItemComments',
});
</script>

<style scoped></style>
