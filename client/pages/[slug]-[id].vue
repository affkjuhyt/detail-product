<template>
    <ItemView :item-detail-data="itemDetailData" />
</template>

<script setup lang="ts">
import ItemView from '~/views/itemView/itemView.vue';

defineComponent({
    name: 'ItemPage',
});

definePageMeta({
    layout: 'default',
});

const route = useRoute();

const id = route.params.id;
const lastElement = Array.isArray(id) ? id[id.length - 1] : id;
console.log('id is: ', lastElement);

const { data, error } = await useCustomFetch(`/item/1/detail`);

if (error.value) {
    showError({
        statusCode: error.value?.data?.statusCode || 404,
        message: error.value?.data?.message,
    });
}

if (!data.value || !data.value.data) {
    showError({
        statusCode: 404,
        message: 'Không tìm thấy sản phẩm.',
    });
}

const itemDetailData = data.value.data;

console.log('itemDetailData: ', itemDetailData)

useHead({
    title: `Lịch sửa giá ${itemDetailData.name}`,
});
</script>

<style scoped></style>
