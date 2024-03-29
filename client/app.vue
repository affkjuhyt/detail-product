<template>
    <a-config-provider
        :locale="viVN"
        :theme="{
            token: {
                colorPrimary: '#ff7227',
            },
        }"
    >
        <a-style-provider hash-priority="high">
            <NuxtLayout>
                <NuxtPage />
            </NuxtLayout>
        </a-style-provider>
    </a-config-provider>
</template>

<script setup lang="ts">
import viVN from 'ant-design-vue/es/locale/vi_VN';
</script>
