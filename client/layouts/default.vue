<template>
    <Header />
    <Breadcrumb />

    <slot />

    <FooterComponent />
</template>

<script setup lang="ts">
import Header from '~/components/header/header.vue';
import FooterComponent from '~/components/footer/footer.vue';

defineComponent({
    name: 'DefaultLayout',
});
</script>

<style scoped></style>
