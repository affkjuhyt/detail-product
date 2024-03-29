<template>
    <client-only>
        <chart :options="chartOptions" />
    </client-only>
</template>

<script setup lang="ts">
import { Chart } from 'highcharts-vue';
import * as Highcharts from 'highcharts';
import dayjs from 'dayjs';
import 'dayjs/locale/vi';
import type { PriceHistory } from '~/types';

dayjs.locale('vi');

const props = defineProps<{
    priceHistoryData: PriceHistory[];
}>();

const categories: string[] = [];

const chartSeries = {
    data: props.priceHistoryData.map((x) => {
        categories.push(x.created_at.toString());

        return x.price;
    }),
};

const chartOptions = ref<Highcharts.Options>({
    title: {
        text: undefined,
    },
    chart: {
        type: 'spline',
        height: 300,
    },
    xAxis: {
        labels: {
            formatter: function () {
                return dayjs(this.value).format('DD - MM - YYYY');
            },
            style: {
                fontSize: '11px',
            },
        },
        showFirstLabel: true,
        categories: categories,
    },
    yAxis: {
        title: {
            text: null,
        },
        labels: {
            style: {
                fontSize: '12px',
            },
        },
    },
    legend: {
        enabled: false,
    },
    tooltip: {
        formatter: function () {
            return `<p class="text-center"><span class="text-xs font-bold">Ngày ${dayjs(this.x).format('DD - MM - YYYY')}</span><br/>
<span class="font-bold">${this.y}đ</span></p>`;
        },
        backgroundColor: '#000000',
        style: {
            color: '#ffffff',
        },
    },
    plotOptions: {
        spline: {
            marker: {
                symbol: 'circle',
            },
        },
    },
    colors: ['#BDBDBD'],
    series: [chartSeries as any],
});
</script>
