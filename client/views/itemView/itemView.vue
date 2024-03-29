<template>
    <div class="container-v2 mt-4">
        <div class="w-full flex items-center lg:items-start flex-col lg:flex-row mb-4 lg:mb-6 px-2 sm:px-0">
            <div class="w-full lg:w-1/2 flex-shrink-0 mr-4 lg:p-6 lg:border rounded-xl leftCol">
                <SlideShow :images="itemDetailData.item.images" />
            </div>

            <div class="flex-grow mx-6 lg:mx-auto w-full lg:w-1/2">
                <ItemInfo :item-detail-data="itemDetailData" />
            </div>
        </div>
        <NavigationBar />
        <PriceComparison />
        <PriceHistory :item-detail-data="itemDetailData" />
        <ItemDescription :description="itemDetailData.item.description" />
        <ItemComments />
        <ItemRelated />
        <ItemRecommended />
        <BlogInItemView :blogs="blogsData"/>
        <ItemSuggest />
        <MetricFrame />
    </div>
</template>

<script setup lang="ts">
import ItemInfo from '~/views/itemView/infoRow/itemInfo.vue';
import SlideShow from '~/views/itemView/infoRow/slideShow.vue';
import NavigationBar from '~/views/itemView/navigationBar.vue';
import PriceComparison from '~/views/itemView/priceComparison/priceComparison.vue';
import PriceHistory from '~/views/itemView/priceHistory/priceHistory.vue';
import ItemDescription from '~/views/itemView/itemDescription/itemDescription.vue';
import ItemComments from '~/views/itemView/comments/comments.vue';
import ItemRelated from '~/views/itemView/itemRelated/itemRelated.vue';
import ItemRecommended from '~/views/itemView/itemRecommended/itemRecommended.vue';
import BlogInItemView from '~/views/itemView/blog/blog.vue';
import ItemSuggest from '~/views/itemView/itemSuggest/itemSuggest.vue';
import MetricFrame from '~/views/itemView/metric/metricFrame.vue';
import type { ItemDetail } from '~/types';
import { useCustomFetch } from '../../composables/useCustomFetch';

defineComponent({
    name: 'ItemView',
});

defineProps<{
    itemDetailData: ItemDetail;
}>();

const blogsData = ref([]);

const { error, data } = await useCustomFetch(`/blog/list`);

console.log('data: ', data);

if (error.value) {
    console.error(error.value);
}

if (data.value) {
    blogsData.value = data.value.data;
}

</script>

<style scoped>
.leftCol {
    max-width: 600px;
    border-color: rgb(208, 208, 208);
}
</style>
